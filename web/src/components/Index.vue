<template>

    <el-container>
        <Slideout class="hidden-lg-and-up" menu="#menu" panel="#panel" :toggleSelectors="['.toggle-button', '.another-toggle', '.and-another']" @on-open="open">
            <nav id="menu">
                <el-row>
                    <el-button class="another-toggle" @click="goToNewContact" type="text" icon="el-icon-circle-plus">
                        New Contact
                    </el-button>
                </el-row>
                <el-row>
                    <el-input
                            placeholder="Search Contacts"
                            prefix-icon="el-icon-search"
                            v-model="searchTerm">
                    </el-input>
                </el-row>
                <ul class="and-another">
                    <li  class="names" v-for="person in data.people">
                        <el-button type="text"  @click="handleClick(person)">{{ person.first_name }} {{ person.last_name }}</el-button>
                    </li>
                </ul>
            </nav>
            <main id="panel">
                <header>
                    <div>
                        <el-button class="toggle-button" style="font-size: 30pt"
                                   type="text"
                                   >☰
                        </el-button>
                    </div>
                </header>
            </main>
        </Slideout>

        <el-aside width="25vw" class="hidden-md-and-down">

            <el-card class="box-card" style="height: 94vh; overflow: scroll">
                <el-row>
                    <el-button @click="goToNewContact" type="text" icon="el-icon-circle-plus">
                        New Contact
                    </el-button>
                </el-row>
                <el-row>
                    <el-input
                            placeholder="Search Contacts"
                            prefix-icon="el-icon-search"
                            v-model="searchTerm">
                    </el-input>
                </el-row>

                <ul>
                    <li @click="handleClick(person)" class="names" v-for="person in data.people">
                        {{ person.first_name }} {{ person.last_name }}
                    </li>
                </ul>
            </el-card>
        </el-aside>
        <el-container>
            <el-main>
                <router-view :updateContacts="updateContacts" />

            </el-main>

        </el-container>


    </el-container>

</template>

<script type="text/babel">
    import axios from 'axios'
    const api_url = 'http://sf.jawn.it/api/';
    import Slideout from 'vue-slideout'
    import 'element-ui/lib/theme-chalk/display.css'

    export default {
        name: 'index',
        data () {
            return {
                bgColor: '#5ED6A8',
                searchTerm: "",
                data: {
                    people: []
                },
                selected: {},
                timeOut: 0,
                isCollapse: true,
                fabActions: [
                    {
                        name: 'alertMe',
                        tooltip: "add contact",
                        icon: 'add_circle'
                    }
                ]
            }
        },
        created () {
            this.updateContacts(null)
        },
        components: {
            Slideout
        },
        watch: {
            '$route' (to, from) {
                if (!this.searchTerm === "") {
                    this.updateContacts(null)
                }
                else if (to.name === "index") {
                    this.updateContacts(null)
                }

            },
            'searchTerm' (query, from) {
                clearTimeout(this.timeOut);

                this.timeOut = setTimeout(() => {
                    this.updateContacts(query)
                }, 250);

            }
        },
        methods: {
            handleClick(person) {
                this.$router.push({
                    name: 'contact',
                    params: {
                        id: person.id
                    }
                })
            },
            open: function () {
                console.log('slideoutOpen')
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            getResources(resource, query) {
                if (query) {
                    return axios.get(api_url + resource + '?qt=' + query)
                }
                return axios.get(api_url + resource)

            },
            goToNewContact(){
                this.$router.push({name: 'create'})
            },
            updateContacts(query) {
                this.getResources('people', query).then(response => {
                    this.data.people = response.data
                }).catch(function (e) {
                    alert(e)
                })
            },
            somethingClicked: function () {
                this.Slideout.toggle()
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
        padding: 3vh;
    }

    .el-aside {
        padding-top: 3vh;
        padding-bottom: 3vh;
        padding-left: 3vh;
        padding-right: 0vh;
        min-width: 350px;
    }

    .names {
        display: block;
        border-bottom: 1px solid #e6ebf5;
        padding-bottom: 10px;
        padding-top: 10px;
        font-size: 13pt;
        cursor: pointer;
    }

    .names:hover {
        background-color: #e8e8e8;
    }

    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        height: 90vh;
    }

    .el-menu--collapse {
        width: 4px;
    }

    .el-radio-group {
        display: inline-block;
        line-height: 1;
        vertical-align: middle;
        font-size: 0;
        z-index: 99;
    }

    .slideout-menu {
        position: fixed;
        top: 0;
        bottom: 0;
        width: 256px;
        height: 100vh;
        overflow-y: scroll;
        -webkit-overflow-scrolling: touch;
        z-index: 0;
        display: none;
        background-color: #FFFFFF;
        color: #585858;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
    }

    .slideout-menu-left {
        left: 0;
    }

    .slideout-menu-right {
        right: 0;
    }

    .slideout-panel {
        background-color: transparent;
        color: white;
        position: absolute;
        z-index: 998;
        min-height: 100vh;
        will-change: transform;
        margin-left: 7px;
        top: -7px;
    }

    .slideout-open,
    .slideout-open body,
    .slideout-open .slideout-panel {
        overflow: hidden;
    }

    .slideout-open .slideout-menu {
        display: block;
        z-index: 997;
    }

    .toggle-button {
        z-index: 999;
    }

</style>
