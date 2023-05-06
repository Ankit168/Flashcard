<template>
    <body class="main-body">
        <div class="container mt-5 mb-5">
            <div class="row justify-content-center">
                <div class="card col-md-4">
                    <h2 class="text-center">Register</h2>
                    <p class="msg">{{ message }}</p>
                    <form @submit.prevent="Register">
                        <div class="form-group">
                            <label>Username: </label>
                            <input id="username" class="form-control" v-model="username" name="username" type="text" placeholder="Enter Your Username" required>
                        </div>
                        <div class="form-group">
                            <label>Password: </label>
                            <input id="password" class="form-control" v-model="password" name="password" type="password" placeholder="Enter Your Password" required>
                        </div>
                        <div class="form-group">
                            <label>Email: </label>
                            <input id="email" class="form-control" v-model="email" name="email" type="email" placeholder="Enter Your Email ID" required>
                        </div>
                        <br>
                        <div>
                            <button type="submit" class="btn">Submit</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </body> 
</template>

<script>
export default {
    name: 'Register',
    methods: {
        async Register() {
            const { username, password, email } = this;
            const res = await fetch(
                "http://127.0.0.1:5000/Register", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ username, password, email })
                }
            );
            const data = await res.json();
            this.$router.push("/login");
            console.log(data);
        }
    }
};
</script>