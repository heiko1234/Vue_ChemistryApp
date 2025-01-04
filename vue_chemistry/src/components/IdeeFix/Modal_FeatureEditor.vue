

<!-- Modal_SumitIdea gets started in IdeeFixCard.vue via isIdeaModalVisible -->

<template>
<div class="modalrapper" v-if="isFeatureEditorModalVisible">
    <div class="backdrop" @click.self="closeFeatureEditorModal">
    <div class="featureeditormodal">
        <div>
            <h1> Submit a new Feature</h1>
            <hr />
            <div class="featureflex">
                <h3>Feature Title</h3>
                <input class="input_text" id="submit_featuretitle" v-model="submit_featuretitle" type="text" />
            </div>
            <div class="featureflex">
                <h3>Feature Description</h3>
                <textarea class="input_text_larger" id="submit_featuredescription" v-model="submit_featuredescription" ></textarea>
            </div>
            <div class="featureflex">
                <h3>Feature Category</h3>
                <select class="input_dropdown" v-model="submit_featurecategory">
                    <option value="Now">Now</option>
                    <option value="Next">Next</option>
                    <option value="Future">Future</option>
                    <option value="Not Categorized">Not Categorized</option>
                </select>
            </div>
            <div class="featureflex">
                <h3>related Ideas</h3>
                <select class="input_dropdown" v-model="selectedIdeas" multiple>
                    <option v-for="idea in ideas" :key="idea[0]" :value="idea[3]">{{ idea[3] }}</option>
                </select>
            </div>
            <div class="featureflex">
                <button class="submit_button" @click="submitFeature">Submit</button>
                <button class="cancel_button" @click.self="closeFeatureEditorModal">Cancel</button>
                <button class="close_button" @click.self="closeFeatureEditorModal">Close</button>
            </div>
        </div>
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import {useToast} from 'vue-toastification';

export default {
name: 'FeatureEditorModal',
props: {
    isFeatureEditorModalVisible: {
    type: Boolean,
    required: true
    }
},
data() {
    return {
    submit_featuretitle: '',
    submit_featuredescription: '',
    submit_featurecategory: 'Not Categorized',
    selectedIdeas: [],
    ideas: []
    }
},
watch: {
    isFeatureEditorModalVisible(newVal) {
        if (newVal) {
            this.searchactiveIdeas();
        }
    }
},
methods: {
    closeFeatureEditorModal() {
    this.submit_featuretitle = '';
    this.submit_featuredescription = '';
    this.submit_featurecategory = 'Not Categorized';
    this.selectedIdeas = [];
    this.$emit('closeFeatureEditorModal')
    console.log('toggleModal closeModal: ', this.isFeatureEditorModalVisible)
    },
    async searchactiveIdeas() {
        try {
            console.log('searchactiveIdeas');
            const response = await axios.get('http://127.0.0.1:8000/api/get_idea_on_status_active');
            this.ideas = response.data;
            console.log('Ideas:', response.data);
        }
        catch (error) {
            console.error('Error searching ideas:', error);
        }
    },
    async submitFeature() {
    console.log('submitFeature')
    const toast = useToast();
        try {
        console.log('Feature get submitted');
        toast.success('Feature submitted.');
        }
        catch (error) {
            console.error('Error submitting feature:', error);
            toast.error('Failed to submit feature.');
        }
    }


}
}
</script>

<style scoped>
.backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 20;
}

.featureeditormodal {
    width: 90%;
    max-width: 40rem;
    background: white;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    z-index: 20;
    overflow: hidden;
}

.featureflex{
    display: flex;
    justify-content: space-between;
    padding: 0 1rem;
    margin: 1rem 0;
}

.input_text{
    width: 80%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
    border-radius: 24px;
}

.input_text_larger{
    width: 80%;
    height: 100px;
    overflow-y: auto;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
    border-radius: 24px;
}

.input_dropdown{
    width: 70%;
    max-width: 80%;
    max-height: 150px;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
    border-radius: 24px;
}

.submit_button {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 20px 10px;
    border: none;
    cursor: pointer;
    width: 80%;
    border-radius: 24px;
}

.cancel_button {
    background-color: #fa9702;
    color: white;
    padding: 14px 20px;
    margin: 20px 10px;
    border: none;
    cursor: pointer;
    width: 80%;
    border-radius: 24px;
}

.close_button {
    background-color: #f44336;
    color: white;
    padding: 14px 20px;
    margin: 20px 10px;
    border: none;
    cursor: pointer;
    width: 80%;
    border-radius: 24px;
}


</style>



