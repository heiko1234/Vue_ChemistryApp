<template>
  <div class="modalrapper" v-if="isIdeaModalVisible">
    <div class="backdrop" @click.self="closeIdeaModal">
      <div class="ideamodal">
        <div>
            <h1> Submit Ideas</h1>
            <hr />
            <div class="ideaflex">
                <h2>Name</h2>
                <input class="input_text" id="submit_name" type="text" />
            </div>
            <div class="ideaflex">
                <h2>Email</h2>
                <input class="input_text" id="submit_email" type="email" />
            </div>
            <div class="ideaflex">
                <h2>Idea Title</h2>
                <input class="input_text" id="submit_ideatitle" type="text" />
            </div>
            <div class="ideaflex">
                <h2>Idea Description</h2>
                <textarea class="input_text_larger" id="sumit_ideadescription" ></textarea>
            </div>
            <div class="ideaflex">
                <button class="submit_button" @click="submitIdea">Submit</button>
                <button class="cancel_button" @click.self="closeIdeaModal">Cancel</button>
                <button class="close_button" @click.self="closeIdeaModal">Close</button>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';

export default {
  name: 'IdeaModal',
  props: {
    isIdeaModalVisible: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    closeIdeaModal() {
      this.$emit('closeIdeaModal')
      console.log('toggleModal closeModal: ', this.isIdeaModalVisible)
    },
    async submitIdea() {
      console.log('submitIdea')
        try {
            console.log('Idea submitted');
            // const response = await axios.post('http://localhost:8000/submit_idea', {
            //     name: this.submit_name,
            //     email: this.submit_email,
            //     short_title: this.submit_ideatitle,
            //     idea_description: this.sumit_ideadescription
            // });
            // console.log('Idea submitted:', response.data);
            this.closeIdeaModal();
        } catch (error) {
            console.error('Error submitting idea:', error);
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
    z-index: 10;
}

.ideamodal {
    width: 90%;
    max-width: 40rem;
    background: white;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    z-index: 10;
    overflow: hidden;
}

.ideaflex{
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
