<template>
    <div class="HomeProductInfo">
        <div class="HomeProductInfoContent">
            <h1 class="HomeTitleAbout"> About </h1>
            <div class="HomeProductInfoContainer">
                <div class="HomeInfoText">
                    <p>
                        {{homeinfotext1}}
                    </p>
                    <p>
                        {{homeinfotext2}}
                    </p>
                    <p>
                        {{homeinfotext3}}
                    </p>
                </div>
                <!-- div for buttons and graphics -->
                <div class="rightInfoContent">
                    <!-- Buttons -->
                    <div class="homeInfoButton">
                        <button class="about_button"
                        :class="{active: selectedButton === 'App1'}"
                        @click="changeGraphic('graphic1')"
                        >
                        App1
                        </button>
                        <button class="about_button"
                        :class="{active: selectedButton === 'App2'}"
                        @click="changeGraphic('graphic2')"
                        >
                        App2
                        </button>
                        <button class="about_button"
                        :class="{active: selectedButton === 'App3'}"
                        @click="changeGraphic('graphic3')"
                        >
                        App3
                        </button>

                    </div>
                    <!-- Graphics -->
                    <div class="HomeInfoGraphic">
                        <img :src="selectedGraphic" alt="Graphic" class="homecontentgraphic" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Apollo from '@/assets/theme/Apollo.jpeg'
import Apollo2 from '@/assets/theme/Apollo2.jpeg'
import Apollo3 from '@/assets/theme/Apollo3.jpeg'

export default {
    name: "HomeAboutInfo",
    props: {
        homeinfotext1: {
            type: String,
            required: true
        },
        homeinfotext2: {
            type: String,
            required: true
        },
        homeinfotext3: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            selectedButton: 'App1',
            selectedGraphic: Apollo
        }
    },
    methods: {
        changeGraphic(graphic) {
            if (graphic === 'graphic1') {
                this.selectedGraphic = Apollo
                this.selectedButton = 'App1'
            } else if (graphic === 'graphic2') {
                this.selectedGraphic = Apollo2
                this.selectedButton = 'App2'
            } else if (graphic === 'graphic3') {
                this.selectedGraphic = Apollo3
                this.selectedButton = 'App3'
            }
        },
        setActiveButton(button) {
            this.selectedButton = button
        }
    },
    mounted() {
        this.changeGraphic('graphic1')
    }

}
</script>

<style>

.HomeProductInfo {
    display: block;
    justify-content: center;
    align-items: center;
    padding: 1rem;
    background-color: white;
}

.HomeProductInfoContent {
    display: block;
    justify-content: center;
    align-items: center;
    background: transparent;
    padding: 1rem;
}

.HomeProductInfoContainer {
    display: flex;
    justify-content: center;
    align-items: center;
    background: transparent;
    padding: 1rem;
}

.HomeTitleAbout {
    font-size: 2rem;
    color: black;
    text-align: center;
    margin-top: 5px;
    margin-bottom: 5px;
    padding: 0;
}

.HomeInfoText {
    flex: 1;
    padding: 1rem;
    font-size: 1rem;
    color: black;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.rightInfoContent {
    display: flex;
    flex: 1;
    justify-content: center;
    align-items: center;
    background: transparent;
    padding: 1rem;
}

.homeInfoButton {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: transparent;
    padding: 1rem;
}

.about_button {
    background-color: transparent;
    color: var(--secondary-color);
    border: 1px solid var(--secondary-color);
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 1rem;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
    padding: 10px 24px;
}

.about_button:hover:not(.active) {
    background-color: var(--secondary-color);
    color: white;
    font-size: 1rem;
    font-weight: bold;
    box-shadow: 0 0 15px var(--secondary-color);
}

.about_button.active {
    background-color: var(--secondary-color);
    color: white;
    font-size: 1rem;
    font-weight: bold;
    box-shadow: 0 0 15px var(--secondary-color);
}

.HomeInfoGraphic {
    display: flex;
    flex: 1;
    justify-content: center;
    align-items: center;
    background: transparent;
    padding: 1rem;
}

.homecontentgraphic {
    width: auto;
    max-height: 500px;
    border-radius: 12px;
}
</style>







