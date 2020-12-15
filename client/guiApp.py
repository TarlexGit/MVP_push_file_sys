from tkinter import *
from tkinter import filedialog, simpledialog
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler 
import watchdog
from transmitter import FileClient
import os
from check_token import checking
# import emoji


class Watchdog(PatternMatchingEventHandler, Observer):
    def __init__(self, path='', token='', patterns='*.test'):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.test'], 
                                                             ignore_directories=True, case_sensitive=False) 
        self.token = token
        Observer.__init__(self)
        self.schedule(self, path=path, recursive=True) 

    def send_data(self, in_file):
        client_token = self.token
        print('key in watch -', client_token)
        data = [] 
        data.append(in_file) 
        client = FileClient('localhost:50051') 
        for x in data: 
            try:
                client.upload(x, client_token)
            except:pass 

    def on_created(self, event): 
        self.send_data(event.src_path)
        print("Watchdog received created event - % s." % event.src_path)  
    
    def on_modified(self, event): 
        print("Watchdog received modified event - % s." % event.src_path)   

    def on_deleted(self, event): 
        print(f"Someone deleted {event.src_path}!") 

    def on_moved(self, event):   
        print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

class GUI:
    def __init__(self):
        self.watchdog = None
        self.watch_path = '.'
        self.root = Tk()
        self.messagebox = Text(width=80, height=10)
        self.messagebox.pack()
        self.token = 'token not set' 
        frm = Frame(self.root)
        Button(frm, text='Browse', command=self.select_path).pack(side=LEFT)
        Button(frm, text='Start Watchdog', command=self.start_watchdog).pack(side=RIGHT)
        Button(frm, text='Stop Watchdog', command=self.stop_watchdog).pack(side=RIGHT) 

        
        Button(frm, text="send Token", bd =5, command=self.set_key).pack(side=LEFT)

        frm.pack(fill=X, expand=1)
        self.root.mainloop()
    

    def start_watchdog(self):
        if self.watchdog is None: 

            if self.watch_path =='.' :
                self.log('Please, change path to forlder') 
                return
            if self.token =='token not set' :
                self.log('Please, set your tokent from http://localhost:8080/dashboard') 
                return

            self.watchdog = Watchdog(path=self.watch_path, token=self.token)
            self.watchdog.start()
            self.log('Watchdog started')

            client_token = self.token
            self.log('Loading files from a folder')

            #### First loading all files from dir path 
            for dirpath, dirs, files in os.walk(self.watch_path): 
                for filename in files:
                    fname = os.path.join(dirpath,filename)
                    print(fname)
                    data = [] 
                    if fname.split('/')[-1].split('.')[-1]=='test':
                        data.append(fname)
                    else: pass 
                    client = FileClient('localhost:50051') 
                    for x in data: 
                        try:
                            client.upload(x, client_token)
                        except:pass  
            
            self.log('loading is complete')
            self.log(' ')
            self.log('--- Monitoring and loading are in progress. Move the files to a folder and they will be displayed on the site. ---')

            # emoji.emojize с :eyes: не пашет, но работает с некоторыми другими. Не рисковать- не добавлять. Пока что.
            #self.log(emoji.emojize('Python is :eyes:'))
        else:
            self.log('Watchdog already started')

    def stop_watchdog(self):
        if self.watchdog:
            self.watchdog.stop()
            self.watchdog = None
            self.log('Watchdog stopped')
        else:
            self.log('Watchdog is not running')

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.watch_path = path
            self.log(f'Selected path: {path}')
        self.stop_watchdog()
        self.start_watchdog()
            
    def set_key(self):
        e = simpledialog.askstring('tok', self.token) 
        if e:
            if checking(e)==200:
                self.token = e
                self.log(f'Token accepted')
            elif checking(e)==404:
                self.log(f'Token is not correct')
            else: self.log(f'непонятный третий вариант и ответ')

    def get_key(self):
        return str(self.token)

    def log(self, message):
        self.messagebox.insert(END, f'{message}\n')
        self.messagebox.see(END)

if __name__ == '__main__':
    GUI()
