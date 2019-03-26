<template>
 <div>
     <p>{{ msg }}</p>
 </div>
</template>


<script>
export default {
    name: 'BioPlate',
    data() {
        return {
            msg: 'Welcome to the lab!',
        };
    },
    methods: {
      getMessage() {
        const path = 'http://localhost:5000/main';
        axios.get(this.path)
            .then((res) => {
                this.msg = res.data;
            })
            .catch((error) => {
                // eslint-diable-next-line
                console.error(error);
            });
        },
    },
    created() {
        this.getMessage();
    },
};
</script>


