 
<template>
    <div>
        <h4>Login</h4>
        <form>
            <label for="username" >username</label>
            <div>
                <input id="username" type="username" v-model="username" required autofocus>
            </div>
            <div>
                <label for="password" >Password</label>
                <div>
                    <input id="password" type="password" v-model="password" required>
                </div>
            </div>
            <div class="margT">
                <b-button variant="success" type="submit" @click="handleSubmit">
                    Login
                </b-button>
            </div>
        </form>
    </div>
</template>
<script>
    export default {
        data(){
            return {
                username : "",
                password : "",
                data:{},
            }
        },
        methods : {
            handleSubmit(e){
                e.preventDefault()
                
                if (this.password.length > 0) {
                    this.$http.post('http://127.0.0.1:8000/api/users/token/', {
                        headers: {
                            "Access-Control-Allow-Origin":"*",
                            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, DELETE',
                            'Access-Control-Allow-Headers': 'X-Requested-With,Accept,Content-Type, Origin'
                        },
                        username: this.username,
                        password: this.password
                    })
                    .then(response => { 
                        localStorage.setItem('user',JSON.stringify(response.data.user))
                        localStorage.setItem('jwt','Bearer '+response.data['access'])
                        // console.log(daresponse.data.access)

                        if (localStorage.getItem('jwt') != null){
                            this.$emit('loggedIn')
                             
                            this.$router.push('dashboard') 
                        }
                    })

                    .catch(function (error) {
                        console.error(error.response);
                    });
                }
            }
        }
    }
</script> 

<style scoped>
    .margT {
        margin-top: 20px;
    }
</style>