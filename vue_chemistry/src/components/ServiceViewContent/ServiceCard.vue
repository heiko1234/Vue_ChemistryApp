

<!-- Card Template -->


<template>
    <div class="service_card">
        <!-- <img :src="computeimageSrc" alt="" class="service_image"> -->
        <!-- <img src="@/assets/tutorials/Apollo4.jpeg" alt=""> -->
        <img :src=CompimageSrc alt="" class="service_image">
        <div class="service_card_text">
            <h2> {{servicetitle}} </h2>
            <h3>{{servicesubtitle}} </h3>
            <div class="service_card_description">
                <p> {{servicedescription}}</p>
            </div>
            <div class="service_buttons">
                <!-- <a class="service_button" :href=servicelink> Start</a> -->
                <button class="service_button" @click="goToService">Start</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ServiceCard',
    props: {
        imageSrc: {
            type: String,
            required: true
        },
        servicetitle: {
            type: String,
            required: true
        },
        servicesubtitle: {
            type: String,
            required: true
        },
        servicedescription: {
            type: String,
            required: true
        },
        servicelink: {
            type: String,
            required: true
        },
    },
    data() {
        return {
        }
    },
    computed: {
        CompimageSrc() {
            try {
                console.log("image loaded")
                console.log(this.imageSrc)
                return this.imageSrc
            }
            catch (error) {
                console.log(error)
                return '@/assets/tutorials/datascience.jpeg'
            }
        }
    },
    methods: {
        goToService() {
            console.log('goToService');
            this.$router.push(this.servicelink)
        }
    }

}
</script>

<style scoped>

.service_card {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    width: 75vw;
    max-width: 650px;
    margin: 10px;
    padding: 44px 30px 44px 20px;
    background: #dadada;
    border: 1px solid #ccc;
    border-radius: 24px;
}


.service_image {
    max-width: 280px;
    width: 36vw;
    height: 300px;
    object-fit: cover;
    margin-left: -60px;
    margin-right: 30px;
    border-radius: inherit;
    box-shadow: 0 60px 40px rgb(0 0 0 / 8%);
    transition: border-radius 0.3s;
}

.service_card h2 {
    font-size: 1.5rem;
    margin-top: 0;
    margin-right: 30px;
    margin-bottom: 10px;
    color: #000000;
}

.service_card h3 {
    font-size: 1.2rem;
    margin: 0;
    opacity: 0.75;
    color: #333;
}

.service_card p {
    font-size: 1rem;
    margin-bottom: 30px;
    opacity: 0.5;
    color: #333;
}

.service_buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
    margin-bottom: 0;
    color: #333;
    padding: 20px;
}

.service_button {
    display: inline-block;
    padding: 10px 20px;
    margin: 30px 40px;
    background: var(--primary-color);
    color: #fff;
    text-decoration: none;
    border-radius: 8px;
    border: 1px solid #333;
}

.service_button:hover {
    background: var(--secondary-color);
    color: #333;
}

</style>
