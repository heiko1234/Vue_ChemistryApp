


<template>
  <div class="promotionheader">

    <h1 class="promotiontitle">
    {{promotion_title_text}}
    </h1>

    <h2 class="promotionsubtitle">

        <span class="promotionsubtitle-halfa">{{promotion_subtitle_texta}}</span>
        <span class="promotionsubtitle-halfb">{{promotion_subtitle_textb}}</span>

    </h2>

  </div>
</template>

<script>
export default {
    name:"promotionheader",
    props: {
        promotion_title_text: {
            type: String,
            required: true
        },
        promotion_subtitle_texta: {
            type: String,
            required: false
        },
        promotion_subtitle_textb: {
            type: String,
            required: false
        }
    }

}
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}

.promotionheader {
  background-color: var(--primary-color);
  display: block;
  align-items: center;
  justify-content: center;
  padding: 5px;
  width: 100%;
}

.promotiontitle {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  color: white;
}

.promotionsubtitle {
  text-align: center;
  font-size: 15px;
}

.promotionsubtitle-halfa {
  color: var(--secondary-color)
}

.promotionsubtitle-halfb {
  color: var(--third-color)
}


</style>


