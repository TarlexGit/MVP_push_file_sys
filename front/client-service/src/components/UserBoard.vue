<template>
    <div class="hello">
        <h1>Page with your data files</h1>
        <h2>{{msg}}</h2>  
        <h3> Your token for descktop app - {{ userToken[0].token }} </h3>

        <div v-for="item in data" :key="item.id" >
            <article>
                <header> 
                    <h2><a >File - {{ item.request_data.split('/')[item.request_data.split('/').length -1] }}<br />
                    </a></h2>
                </header>

                <div>
                    <b-table striped hover :items="BroFunc(item.content.slice(8, 100).split(/[\s ]+/))">dwadawd</b-table>
                </div>  
            </article>
        </div>
    </div>
</template>
 
<script>
    import 'bootstrap/dist/css/bootstrap.css'
    import 'bootstrap-vue/dist/bootstrap-vue.css'
    export default {
        data () {
            return {
                msg: 'Files:',
                data:{},
                newData:[],
                dynamicSlice:111,
                userToken:'',
            }
        },
        created () { 
            this.handleSubmit(), 
            this.getUserToken()
        }, 
        methods : {
            handleSubmit(){ 
                let tok = localStorage.getItem('jwt'); 
                this.$http.get('http://127.0.0.1:8000/api/users/user/files/', { 
                    headers: {
                        Authorization: tok
                    }, 
                })
                .then(response => { 
                    this.data = response.data;
                    console.log(this.data);
                })

                .catch(function (error) {
                    console.error(error.response);
                }); 
            },

            getUserToken() {
                let tok = localStorage.getItem('jwt'); 
                this.$http.get('http://127.0.0.1:8000/api/users/user/token/', { 
                    headers: {
                        Authorization: tok
                    }, 
                })
                .then(response => { 
                    this.userToken = response.data;
                    console.log('token');
                    console.log(this.userToken);
                })

                .catch(function (error) {
                    console.error(error.response);
                }); 
            },

            BroFunc(arr) { 
                const res = [];
                arr.toString().replace(/[\n\r]/g," ")
                console.log('arr')
                console.log(arr)
                for (let i = 0; i < arr.length; i++) {
                res.push({
                    ...arr[i] !== undefined ? { x: arr[i] } : {},
                    ...arr[i + 1] !== undefined ? { y: arr[i + 1] } : {},
                    ...arr[i + 2] !== undefined ? { z: arr[i + 2] } : {}, 
                    ...arr[i + 3] !== undefined ? { i: arr[i + 3] } : {}, 
                    })
                    i += 3;
                }
                this.newData = res
                // console.log(this.newData)
                return res;
            },
            
        }
    }
</script>
  
<style scoped>
    h1, h2 {
        font-weight: normal;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #42b983;
    }

    .v-table {
        max-width: 900px;
        margin: 0 auto;
    }
    
    .v-table_header {
        display: flex;
        justify-content: space-around;
    }

    .v-table-row {
        display: flex;
        justify-self: space-around;
    }
</style> 