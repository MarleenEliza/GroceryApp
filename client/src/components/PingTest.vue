<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";

export default Vue.extend({
  name: "Ping",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getMessage() {
     console.log('getting message...');
      const path = "http://localhost:5000/ping";
      axios
        .get(path)
        .then((response) => {
          this.msg = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getMessage();
  },
});

// name: 'Ping',
//   data() {
//     return {
//       msg: '',
//     };
//   },
//   methods: {
//     getMessage() {
//       const path = 'http://localhost:5000/ping';
//       axios.get(path)
//         .then((res) => {
//           this.msg = res.data;
//         })
//         .catch((error) => {
//           // eslint-disable-next-line
//           console.error(error);
//         });
//     },
//   },
//   created() {
//     this.getMessage();
//   },
</script>
