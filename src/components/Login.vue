<template>
    <body>
        <div class="container mt-5 mb-5" :style="{'background-image':`url(../assets/background_image.jpeg)`}">
            <div class="row justify-content-center">
                <div class="card col-md-4 p-2">
                    <h2 class="text-center">
                        FLASHCARD
                        <br> Login
                    </h2>
                    <form @submit.prevent="login">
                        <div class="form-group">
                            <label>Username: </label>
                            <input id="username" class="form-control" v-model="username" name="username" type="text" placeholder="Enter Your Username" required>
    
                        </div>
                        <div class="form-group">
                            <label for="back">Password </label>
                            <input class="form-control" v-model="password" name="password" type="password" placeholder="Enter Your Password" required>
                        </div>
                        <br>
                        <div>
                            <button type="submit" class="btn" style= "margin-left:14px !important">Submit</button>
                            <a href= "/register" class="btn" style= "margin-left:14px !important">Register</a>
                        </div>
                        <div>
                          
                        </div>
                    </form>
    
                </div>
                <div>
                    
                </div>
            </div>
        </div>
    </body>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
    name: 'Login',
    data() {
        return {
            username: "",
            password: "",
            // products: {}
        };
    },
    computed: {
        // ...mapState({
        //     currentUser: (state) => state
        // }),
        ...mapGetters(['isUserLoggedIn'])
    },
    methods: {
        ...mapActions(['initLogin']),
        login() {
            console.log('ss');
            this.initLogin({
                username: this.username,
                password: this.password
            });
            // const res = await fetch(
            //     "http://127.0.0.1:5000/login", {
            //         method: "POST",
            //         headers: {
            //             "Content-Type": "application/json"
            //         },
            //         body: JSON.stringify({
            //             username: this.username,
            //             password: this.password,
            //         })
            //     }
            // );
            // const data = await res.json();
            // this.$router.push("/dashboard");
            // console.log(data);
        }
    },
    watch: {
        isUserLoggedIn: function(newValue) {
            if (newValue) {
                this.$router.push("/dashboard");
            }
        }
    },
    mounted() {
        if (this.isUserLoggedIn) {
            this.$router.push("/dashboard");
        }
    },
};
</script>


<style scoped>
.btn {
    padding: 10px 40px;
    background-color: #236B8E;
    color: #FFFFFF;
    font-weight: bold;
    border-radius: 10px;
    margin-left: 140px;
}

.textbox {
    padding: 10px 40px;
    background-color: #236B8E;
    text-decoration-color: #FFFFFF;
    border-radius: 10px;
}

.word {
    color: #FFFFFF;
    font-style: oblique;
    font-weight: bold;
}

.main-body {
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
}
</style>