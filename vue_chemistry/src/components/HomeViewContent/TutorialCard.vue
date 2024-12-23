<template>
    <div class="tutcard">
        <div class="tutcardtag">
        {{tuttag}}
        </div>
        <!-- <img :src="require(`@/assets/tutorials/${tutimage}`)" alt="imageName" class="tutcardimage"> -->
        <!-- <img src="@/assets/tutorials/datascience.jpeg" alt="imageName" class="tutcardimage"> -->
        <!-- # image get not loaded with require -->
        <img :src="imageSrc" alt="imageName" class="tutcardimage">

        <h2> {{tuttitle}} </h2>
        <!-- <p>{{imageSrc}}</p> -->
        <div class="tutcarddescription">
            <p> {{tutcarddescription}}</p>
        </div>
    </div>

</template>

<script>
export default {
    name: 'TutorialCard',
    props: {
        tuttag: {
            type: String,
            required: true
        },
        tutimage: {
            type: String,
            required: true
        },
        tuttitle: {
            type: String,
            required: true
        },
        tutcarddescription: {
            type: String,
            required: true
        }
    },
    computed: {
        imageSrc() {
            try {
                // return '@/assets/tutorials/datascience.jpeg'
                // return require(`@/assets/tutorials/${this.tutimage}`)
                return `@/assets/tutorials/${this.tutimage}`
            }
            catch (error) {
                console.log(error)
                return '@/assets/tutorials/datascience.jpeg'
            }
        }
    }

}
</script>

<style scoped>

.tutcard {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 200px;
    min-width: 200px;
    height: 250px;
    padding: 20px;
    margin: 5px 20px;
    border: 1px solid #ccc;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    position: relative;
    overflow: hidden;
    cursor: pointer;
}

.tutcardtag {
    padding: 4px 8px;
    background-color: var(--secondary-color);
    color: white;
    border-radius: 4px;
    align-self: flex-start;
    margin: 8px;
    position: absolute;
    top: 12px;
    left: 12px;
    z-index: 1;
}

.tutcardimage {
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 20px;
}

.tutcarddescription {
    padding: 5px;
    text-align: center;
}

</style>