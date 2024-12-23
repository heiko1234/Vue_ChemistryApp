
<template>
  <div class="service_header">

    <div class="service_header_items">
        <div class="hhi_left">
            <img src="@/assets/theme/Apollo.jpeg" alt="Logo" class="logo" @click="goToMainPage">

        </div>

    </div>
    <div class="separator">
        <hr/>
    </div>

  </div>
</template>

<script>
export default {
    name: "serviceheader",
    methods: {
        goToMainPage() {
            console.log('goToMainPage');
            this.$router.push('/')
        }
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


.service_header {
    background-color: transparent;
    display: block;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 100%;
    height: 60px;
}


.service_header_items {
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
    width: 100%;
}


.separator {
    width: 100%;
    height: 2px;
    background-color: black;
    margin: 0;
    padding: 0;
}

</style>





