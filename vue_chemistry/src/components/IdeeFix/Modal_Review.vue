
<!-- Modal_Review gets started in IdeeVoteCard.vue via isReviewModalVisible -->

<template>
  <div class="modalrapper" v-if="isReviewModalVisible">
    <div class="backdrop" @click.self="closeReviewModal">
      <div class="reviewmodal">
        <h1>Idea Review</h1>
        <hr />
        <h4 class="text_closer"> Use a filter</h4>
        <div class="stacked_flex">
          <div class="stacked_block">
            <h3>Name</h3>
            <input type="text" class="input_text" id="review_name" v-model="review_name" />
          </div>
          <div class="stacked_block">
            <h3>Idea Title</h3>
            <input type="text" class="input_text" id="review_ideatitle" v-model="review_ideatitle" />
          </div>
          <div class="stacked_block">
            <h3>Idea Description</h3>
            <input class="input_text" id="review_ideadescription" v-model="review_ideadescription" />
          </div>
        </div>
        <hr />
        <div class="scrollable">
          <div>
          <!-- Table output -->

            <h4>Search Results</h4>
            <table v-if="ideas.length">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Title</th>
                  <th>Description</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idea in ideas" :key="idea.idea_id">
                  <td>{{ idea[0] }}</td>
                  <td>{{ idea[1] }}</td>
                  <td>{{ idea[2] }}</td>
                  <!-- <td>{{ idea.name }}</td>
                  <td>{{ idea.short_title }}</td>
                  <td>{{ idea.idea_description }}</td> -->
                </tr>
              </tbody>
            </table>
            <p v-else>No results found</p>

            <!-- Table end -->

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {

  name: 'ReviewModal',
  props: {
    isReviewModalVisible: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      review_name: '',
      review_ideatitle: '',
      review_ideadescription: '',
      ideas: []
    }
  },
  watch: {
    review_name(newVal) {
      this.searchIdeas();
    },
    review_ideatitle(newVal) {
      this.searchIdeas();
    },
    review_ideadescription(newVal) {
      this.searchIdeas();
    }
  },

  methods: {
    closeReviewModal() {
      this.$emit('closeReviewModal');
    },
    async searchIdeas() {
      try {
        console.log('searchIdeas');
        const response = await axios.post('http://127.0.0.1:8000/api/get_active_ideas_filtered', {
            name: this.review_name,
            short_title: this.review_ideatitle,
            idea_description: this.review_ideadescription
        });
        this.ideas = response.data;
        console.log('Ideas:', response.data);
      }
      catch (error) {
        console.error('Error fetching ideas:', error);
      }
    }
  },
  // mounted() {
  //   this.searchIdeas();
  // }

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

.reviewmodal {
    width: 90%;
    max-width: 40rem;
    background: white;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    z-index: 10;
    overflow: hidden;
}

.stacked_block{
  display: block;
  margin: 0;
  padding: 10px;
}

.stacked_flex {
    display: flex;
    justify-content: space-between;
    padding: 0;
    padding-bottom: 10px;
}

.stacked_flex h3 {
  margin: 5px;
  padding: 5px;
}

.text_closer {
  text-align: left;
  margin: 5px;
  padding: 5px;
}

.scrollable {
  overflow-y: auto;
  max-height: 600px;
  min-height: 400px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #f5f5f5;
}

</style>
