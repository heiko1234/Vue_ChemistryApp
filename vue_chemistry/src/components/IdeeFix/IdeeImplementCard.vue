<template>
    <div class="card-container">
        <img src="@/assets/service_pics/Asterix_Zaubertrank.jpeg" alt="" :class="{ 'disabled_image': !isButtonActive }" class="service_image">
        <div class="service_card_text">
            <h2> {{servicetitle}} </h2>
            <h3>{{servicesubtitle}} </h3>
            <div class="service_card_description">
                <p> {{servicedescription}}</p>
            </div>
            <div class="service_buttons">
                <!-- <a class="service_button" :href=servicelink> Start</a> -->
                <button class="service_button" @click="startFeatureEngineering" :disabled="!isButtonActive">Start</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "IdeeFixCard",
    data() {
        return {
            servicetitle: "Feature Managing",
            servicesubtitle: "New Features for our services",
            servicedescription: "Feature Requests get managed here by the Developer Team",
            isButtonActive: true,
        }
    },
    methods: {
        startFeatureEngineering() {
            console.log('startFeatureEngineering');
        }
    }

}
</script>

<style scoped>

.card-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #f1f1f1;
    border: 1px solid  #000000;
    border-radius: 8px;
    padding: 20px;
    width: 300px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 20px;
}

.service_image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 16px;
    margin-bottom: 20px;
}

.disabled_image {
    filter: grayscale(100%);
}

.service_card_text h2 {
    margin-top: 0;
    font-size: 1.5rem;
}

.service_card_text h3 {
    font-size: 1.2rem;
    margin: 0;
    opacity: 0.75;
    color: #333;
}

.service_card_description p {
    font-size: 1rem;
    margin-bottom: 30px;
    opacity: 0.6;
    color: #333;
}

.service_buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

.service_button {
    display: inline-block;
    padding: 10px 20px;
    background: #4CAF50;
    color: white;
    text-decoration: none;
    border-radius: 8px;
    border: 1px solid #4CAF50;
    cursor: pointer;
}

.service_button:hover {
    background-color: var(--secondary-color);
}

.service_button:disabled {
    background: #ccc;
    border: 1px solid #ccc;
    cursor: not-allowed;
}


</style>