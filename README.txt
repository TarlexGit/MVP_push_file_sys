front/ – Авторизация пользователя, регистрация, отображение загруженных файлов.
back/ – получает от агента файлы .test кладет содержимое в базу данных. Отдает список фронту.  
client/ – следит за указанной папкой на локальной машине, файлы .test отправляет на сервер.
.test файлы генерим по скрипту client/create_client_files/create_data.py 


Инструкция по применению
1) git clone https://github.com/TarlexGit/MVP_push_file_sys.git

Билдим десктопную прогу
* все на python3.8.6
python venv env-client
cd MVP_push_file_sys/client
pip install -r req.txt

создадим файл для отправки (после - добавьте его в папку, которую собираетесь отслеживать в приложении)
cd create_client_files/
python create_data.py
cd ..

pyinstaller guiApp.py --onefile  
в /dist будет запскаемое приложение. Если не запускается, перенесите на раб. стол или 
создайте ярлык с ссылкой на этот файл, в линукс шаблоны имен файлов + *.sh *.so. 
( ^->билдится под систему, запускается по клику.)
(https://pyinstaller.readthedocs.io/en/stable/index.html)

2) качаем докер контейнеры (либо используйте докер-файлы из back/, front/)
docker pull tarlex/mvp_fs_back
docker pull tarlex/mvp_fs_front


3) После загрузки контейнеров:

run backend: 
docker run -p 8000:8000 -p 50051:50051 tarlex/mvp_fs_back 
первый порт для django->front, второй для django-grpc-framework->client 

run frontend
docker run -it -p 8080:80 --rm --name vue-nginx-mvp tarlex/mvp_fs_front

в браузере - http://localhost:8080/
регистрация: логин - userone, пароль - useroneuserone, подтверждение - useroneuserone

Копируем ключ на странице и запускаем guiApp (из шага 2) (двойной клик или в консоли ./guiApp). 
По кнопке 'send Token' вводим ключ с сайта, клик -> 'ок'. 
Кнопка 'Browse' выбираем папку, слежка начинается сразу при выборе пути, 
от самой папки по всем вложенным. Кнопки справа управляют смотрящим. 
При добавлении файлов отправляет на сервер. На фронте показ строк ограничен.


