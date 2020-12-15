 
<template> 
 <div>
    <h4>Register</h4>
        <form>
            <label for="username">Name</label>
            <div>
                <input id="username" type="text" v-model="username" required autofocus>
            </div>
 
            <label for="email" >E-Mail Address</label>
            <div>
                <input id="email" type="email" v-model="email" required>
            </div>
 
            <label for="password">Password</label>
            <div>
                <input id="password" type="password" v-model="password" required>
            </div>
 
            <label for="password-confirm">Confirm Password</label>
            <div>
                <input id="password-confirm" type="password" v-model="password_confirmation" required>
            </div> 
 
            <div>
                
                <button type="submit" @click="handleSubmit"> 
                    Registration
                </button>
                
            </div>
        </form>
    </div>
</template>
 
<script>
    export default {
        // props : ["nextUrl"],
        data(){
            return {
                username : "",
                email : "",
                password : "",
                password_confirmation : "", 
            }
        },
        methods : {
            handleSubmit(e) {
                // let data = {
                //     username: this.username,
                //     email: this.email,
                //     password: this.password
                // };
                e.preventDefault() 

                if (this.password === this.password_confirmation && this.password.length > 0)
                {
                    let url = "http://127.0.0.1:8000/api/users/auth/users/"
                     
                    this.$http.post(url,{
                        username: this.username,
                        email: this.email,
                        password: this.password, 
                    })
                    .then(function (response) {
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
                } else {
                    this.password = ""
                    this.passwordConfirm = ""
 
                    return alert("Passwords do not match")
                }
                this.$router.push('/login')
            },
            submit(){
                //if you want to send any data into server before redirection then you can do it here
                this.$router.push("/login");
            }
        }
    }
</script> 