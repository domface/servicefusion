<template>

    <el-container>
        <el-main>
            <create-contact></create-contact>

        </el-main>


    </el-container>

</template>

<script type="text/babel">
    import axios from 'axios'
    import CreateContact from './CreateContact.vue'
    const api_url = 'http://sf.jawn.it/api/'
    import fab from 'vue-fab'

    export default {
        name: 'create',
        data () {
            return {
                bgColor: '#5ED6A8',

                data: {
                    people: []
                }
            }
        },
        created () {
        },
        components: {
            CreateContact
        },
        methods: {
            handleClick(row, event, column) {
                this.selected = row
            },
            createResource(resource) {
                axios({
                    method: 'post',
                    url: api_url + resource + '/',
                    data: {
                        firstName: 'Fred',
                        lastName: 'Flintstone'
                    }
                })
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
    }

    a {
        color: #42b983;
    }

    .el-main {
        padding: 0px;
    }

    .el-aside {

    }


</style>
