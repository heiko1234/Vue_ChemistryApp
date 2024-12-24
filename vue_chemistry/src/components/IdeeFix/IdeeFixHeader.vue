
<template>
  <div class="ideefix_header">

    <div class="ideefix_header_items">
        <div class="hhi_left">
            <img src="@/assets/theme/Apollo.jpeg" alt="Logo" class="logo" @click="goToMainPage">
        </div>

        <div class="hhi_center">
            <h2 :class="headerClass">{{ headerText }}</h2>
        </div>

        <div class="hhi_right">

        <!-- # make a drop down menu -->
            <!-- <div class="dropdown">
                <button class="dropbtn">Menu</button>
                <div class="dropdown-content">
                    <ul>Developer</ul>
                    <ul>Admin</ul>
                </div>
            </div> -->

            <div class="dropdown">
                <button class="dropbtn">{{ selectedRole }}</button>
                <div class="dropdown-content">
                    <a @click="selectRole('Developer')">Developer</a>
                    <a @click="selectRole('Admin')">Admin</a>
                    <a @click="selectRole('User')">User</a>
                </div>
            </div>

        </div>

    </div>
    <div class="separator">
        <hr/>
    </div>

  </div>
</template>

<script>
export default {
    name: "ideefixheader",
    methods: {
        goToMainPage() {
            console.log('goToMainPage');
            this.$router.push('/')
        },
        selectRole(role) {
                this.selectedRole = role;
                this.$emit("roleSelected", role);
                switch(role) {
                    case "Developer":
                        this.headerText="Welcome Developer";
                        this.headerClass="developer-header";
                        break;
                    case "Admin":
                        this.headerText="Welcome Admin";
                        this.headerClass="admin-header";
                        break;
                    case "User":
                        this.headerText="Welcome User";
                        this.headerClass="user-header";
                        break;
                    default:
                        this.headerText="Default"
                        this.headerClass="default-header"
                }
            }
        },
    data() {
        return {
            selectedRole: 'User',
            headerText: "Welcome User",
            headerClass: "user-header"
        };
    }

}
</script>

<style scoped>

body {
    margin: 0;
    font-family: Arial, sans-serif;
}

.logo {
    width: 50px;
    height: 50px;
    border-radius: 50%;
}

.logo:hover {
    transform: scale(1.07);
    cursor: pointer;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}


.ideefix_header {
    background-color: transparent;
    display: block;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 100%;
    height: 60px;
}


.ideefix_header_items {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px;
    width: 100%;
}

.hhi_left {
    display: flex;
    justify-content: left;
    align-items: center;
    padding: 5px;
    width: 30%;
}

.hhi_center {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 5px;
    width: 40%
}

.hhi_right {
    display: flex;
    justify-content: right;
    align-items: center;
    padding: 5px;
    margin-right: 50px;
    width: 30%
}

.separator {
    width: 100%;
    height: 2px;
    background-color: black;
    margin: 0;
    padding: 0;
}

.user-header {
    color: blue;
}

.developer-header {
    color: green;
}

.admin-header {
    color: red;
}

.default-header {
    color: orchid;
}


.dropdown {
    position: relative;
    display: inline-block;
}

.dropbtn {
    background-color: #4CAF50;
    color: white;
    width: 150px;
    padding: 16px;
    font-size: 16px;
    border: none;
    border-radius: 20px;
    cursor: pointer;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
    background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}

</style>





