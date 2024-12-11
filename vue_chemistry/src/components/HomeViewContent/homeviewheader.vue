


<template>
  <div class="homeview_header">

    <div class="homeview_header_items">
        <div class="hhi_left">
            <a href="">
                <img src="@/assets/theme/Apollo.jpeg" alt="Logo" class="logo">
            </a>

            <div class="hhi_middle">
                <button class="middle_left_button" @click="scrollToSection('About')">About</button>
                <button class="middle_left_button" @click="scrollToSection('Tutorials')">Tutorials</button>

            </div>

        </div>

        <div class="hhi_right">
            <button class="middle_right_button" @click="openModal">Contact</button>
            <button class="start_button" @click="$router.push('/services')">Get Started</button>
        </div>

    </div>
    <div class="separator">
        <hr/>
    </div>

  </div>
</template>

<script>
export default {
    name: "homeviewheader",
    methods: {
        scrollToSection(section) {
            this.$emit('scroll-to-section', section)
        },
        openModal() {
            this.$emit('open-contact-modal')
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


.homeview_header {
    background-color: transparent;
    display: block;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 100%;
    height: 60px;
}


.homeview_header_items {
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

.middle_left_button {
    background-color: transparent;
    border: none;
    color: black;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
    padding: 10px 24px;
}

.middle_left_button:hover {
    text-decoration: underline;
    color: var(--secondary-color);
}

.hhi_right {
    display: flex;
    justify-content: right;
    align-items: center;
    padding: 5px;
    margin-right: 15px;
    width: 100%;
}

.middle_right_button {
    background-color: transparent;
    border: none;
    color: black;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
    padding: 10px 24px;
}

.middle_right_button:hover {
    text-decoration: underline;
    color: var(--secondary-color);
}

.start_button {
    background-color: var(--primary-color);
    border: none;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
    padding: 10px 16px;
}

.start_button:hover {
    background-color: green;
    color: white;
    font-weight: bold;
    border: 2px solid rgb(0, 128, 0);
    box-shadow: 0 0 15px rgba(0 128, 0, 0.685);
}


.separator {
    width: 100%;
    height: 2px;
    background-color: black;
    margin: 0;
    padding: 0;
}

</style>





