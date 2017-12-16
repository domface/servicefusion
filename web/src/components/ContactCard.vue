<template>
    <el-row align="middle">
        <el-col>
            <el-card class="box-card" style="height: 94vh; overflow: scroll">

                <div slot="header" class="clearfix">
                    <el-button class="danger" style="float: right; padding: 8px 7px" @click="deleteContact(person.id)"
                               type="text"
                               icon="el-icon-delete">Delete Contact
                    </el-button>

                </div>


                <el-form ref="person" :model="person" label-width="100px">
                    <div class="text item">

                        <el-row>

                        </el-row>

                        <div v-if="!edit.info">
                            <el-row  type="flex" justify="middle" align="middle">
                                <el-col :span="6" style="text-align: left">
                                    <div class="caption">

                                    </div>
                                </el-col>
                                <el-col style="text-align: left">
                                    <h2>{{ person.first_name }} {{ person.last_name }}</h2>
                                </el-col>
                                <el-col :span="4" style="text-align: right">
                                    <el-tooltip class="item" effect="light" content="Edit Info" placement="left-start">
                                        <el-button v-if="!edit.info"
                                                   class="button-pad"
                                                   size="medium"
                                                   type="text"
                                                   icon="el-icon-edit"
                                                   @click="editInfo"></el-button>

                                    </el-tooltip>
                                    <el-button-group v-if="edit.info">
                                        <el-button class="button-pad danger"
                                                   type="text"
                                                   icon="el-icon-error"
                                                   @click="editInfo"
                                        ></el-button>
                                        <el-button type="text"
                                                   class="button-pad success"
                                                   icon="el-icon-success"
                                                   @click="update('person', person)"></el-button>

                                    </el-button-group>
                                </el-col>
                            </el-row>
                            <el-row  type="flex" justify="start" align="middle">
                                <el-col :span="6" style="text-align: left">
                                    <div  class="title-padding">
                                        Birthday
                                    </div>
                                </el-col>
                                <el-col style="text-align: left">
                                    <div>
                                        {{ person.date_of_birth | moment("MMMM Do YYYY")}}
                                    </div>
                                </el-col>
                                <el-col :span="4" style="text-align: right"></el-col>
                            </el-row>


                        </div>


                        <el-row v-if="edit.info" :gutter="16" justify="space-between">
                            <el-form-item label="First Name"

                                          :rules="{required: true, message: 'Please Enter a First Name', trigger: 'blur'}"
                                          prop="first_name">
                                <el-input :disabled="!edit.info" placeholder="First Name"
                                          v-model="person.first_name"></el-input>
                            </el-form-item>
                            <el-form-item label="Last Name"
                                          :rules="{required: true, message: 'Please Enter a Last Name', trigger: 'blur'}"
                                          prop="last_name">
                                <el-input :disabled="!edit.info" placeholder="Last Name"
                                          v-model="person.last_name"></el-input>
                            </el-form-item>
                            <div class="">
                                <el-form-item label="Birthday"
                                              :rules="{ pattern:/^\d{4}-\d{2}-\d{2}$/, required: true, message: 'Please add a birthday', trigger: 'blur'}"
                                              prop="date_of_birth">
                                    <el-date-picker
                                            :disabled="!edit.info"
                                            v-model="person.date_of_birth"
                                            type="date"
                                            placeholder="Birth Date"
                                            value-format="yyyy-MM-dd">
                                    </el-date-picker>
                                </el-form-item>
                            </div>
                        </el-row>


                    </div>
                </el-form>


                <!--   ADDRESSES   --->
                <addresses :person="person.id"
                           :addresses="person.addresses"
                           :pluralize="pluralize"
                           :updateResource="updateResource"
                           :createResource="createResource"
                           :updateUi="updateUi"
                           :deleteResource="deleteResource"
                           :del="del"></addresses>


                <phone-numbers :person="person.id"
                               :numbers="person.phone_numbers"
                               :pluralize="pluralize"
                               :updateResource="updateResource"
                               :createResource="createResource"
                               :updateUi="updateUi"
                               :deleteResource="deleteResource"
                               :del="del"></phone-numbers>


                <emails :person="person.id"
                        :emails="person.emails"
                        :pluralize="pluralize"
                        :updateResource="updateResource"
                        :createResource="createResource"
                        :updateUi="updateUi"
                        :deleteResource="deleteResource"
                        :del="del"></emails>


            </el-card>
        </el-col>
    </el-row>
</template>

<script type="text/babel">
    import axios from 'axios'
    import Addresses from './Addresses.vue'
    import PhoneNumbers from './PhoneNumbers.vue'
    import Emails from './Emails.vue'

    export default {
        name: 'contact-card',
        props: ['updateContacts'],
        created () {
            this.updateUi()

        },
        data () {
            return {
                edit: {
                    info: false
                },
                add: {
                    phone_number: false,
                    email: false,
                    address: false
                },
                new: {
                    phone_number: {
                        number: null,
                        type: null,
                        edit: true
                    },
                    email: {
                        email: "",
                        edit: true
                    },
                    address: {
                        street: "",
                        street_2: "",
                        city: "",
                        state: "",
                        zip: "",
                        edit: true
                    }
                },
                person: {}
            }
        },
        watch: {
            '$route' (to, from) {
                this.updateUi()
            }
        },
        components: {
            Addresses,
            PhoneNumbers,
            Emails
        },
        methods: {

            ///// methods for calling API ///

            update(resource, data, index) {
                let r_plural = this.pluralize(resource)
                data['person_id'] = this.person.id
                this.updateResource(r_plural, data).then(response => {
                    this.updateUi()
                    this.updateContacts()
                    this.$message({
                        type: 'success',
                        message: 'Contact Updated'
                    })
                }).catch(e => {
                    this.$message({
                        type: 'danger',
                        message: 'Error'
                    })
                })
                if (resource !== 'person') {
                    this.$set(this.person[r_plural][index], "edit", false)
                }
                else {
                    this.edit.info = false
                }


            },
            save(resource, data) {
                this.$refs[resource].validate((valid) => {
                    if (valid) {
                        let r_plural = this.pluralize(resource)
                        let new_data = data.slice(-1)[0]
                        let index = data.length - 1
                        new_data['person_id'] = this.person.id
                        this.createResource(r_plural, new_data)
                        this.add[resource] = false
                        this.$set(this.person[r_plural][index], "edit", false)
                        this.getResource('people', this.person.id)
                                .then(response => {
                                    this.person = response.data
                                }).catch(e => {
                            this.$message({
                                type: 'danger',
                                message: 'Error'
                            });
                        })
                    } else {
                        return false;
                    }
                })
            },
            del(resource, data, index) {
                let r_plural = this.pluralize(resource)
                if (resource === 'phone_number' || resource === 'email') {
                    if (this.person[r_plural].length < 2) {
                        this.$alert('You must have at least one ' + resource.replace('_', ' ') + ' for each contact.', 'Error', {
                            confirmButtonText: 'OK'

                        });
                        return false;
                    }
                }

                this.deleteResource(r_plural, data.id)
            },

            editInfo() {
                if (this.edit.info === true) {
                    this.edit.info = false
                }
                else if (this.edit.info === false) {
                    this.edit.info = true
                }
            },


            ///////// helper functions
            pluralize(resource) {
                let r_plural;
                if (resource === 'address') {
                    r_plural = 'addresses'
                }
                else if (resource === 'person') {
                    r_plural = 'people'
                }
                else {
                    r_plural = resource + 's'
                }
                return r_plural
            },


            createResource(resource, data) {
                return axios.post(resource + "/", data)


            },
            updateResource(resource, data) {
                return axios.patch(resource + '/' + data.id.toString() + '/', data)

            },
            deleteContact(id) {
                this.$confirm('This will permanently delete the contact. Continue?', 'Warning', {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                    center: true
                }).then(() => {
                    this.deleteResource('people', id)
                    this.$message({
                        type: 'success',
                        message: 'Delete completed'
                    });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: 'Delete canceled'
                    });
                });
            },


            getResource(resource, id) {
                return axios.get(resource + '/' + id.toString() + '/')
            },


            deleteResource(resource, id) {
                axios({
                    method: 'delete',
                    url: resource + "/" + id.toString() + "/"
                })
                        .then(response => {
                            if (resource === 'people') {
                                this.$router.push({
                                    path: '/'
                                })
                                this.$message({
                                    type: 'success',
                                    message: 'Contact Deleted'
                                });
                                return false
                            }

                            this.$message({
                                type: 'success',
                                message: 'Contact Updated'
                            });
                            this.updateUi()
                        })
                        .catch(e => {
                            this.$message({
                                type: 'danger',
                                message: 'Error'
                            });
                        })
            },
            updateUi() {
                this.getResource('people', this.$route.params.id)
                        .then(resp => {
                            this.person = resp.data;
                        })
                        .catch(err => {
                            this.$message({
                                type: 'danger',
                                message: err
                            })
                        })

            }
        }
    }
</script>

<style>
    .contact-form {
        display: inline-block;
        vertical-align: middle;
    }

    .section_heading {
        border-bottom: 1px solid #e6ebf5;
        margin-bottom: 10px;
        margin-top: 20px;
        padding-top: 5px;
        font-size: 12pt;

    }

    .el-date-editor.el-input {
        width: 100%;
    }

    .el-input {
        padding-top: 7px;
    }

    .el-dropdown-link {
        cursor: pointer;
        color: #409EFF;
    }

    .el-icon-arrow-down {
        font-size: 12px;
    }

    .address-divider {
        padding-bottom: 10px;
        padding-top: 5px;
        margin-bottom: 10px;
        margin-top: 5px;
    }

    .button-pad {
        margin-bottom: 5px;
        padding: 5px;
    }

    .el-input.is-disabled .el-input__inner {
        background-color: #ffffff;
        border-color: #ffffff;
        color: #4d5057;
        cursor: default;
    }

    .el-card__header {
        border: 0px;
    }

    .el-form-item.is-required .el-form-item__label:before {
        content: '';
        color: #fffdf4;
        margin-right: 4px;
    }

    .el-form-item {
        margin-bottom: 8px;
    }

    .el-form-item__label {
        font-size: 9pt;
    }

    .danger {
        color: #fa5555;
    }

    .success {
        color: #67c23a;
    }

    @media screen and (min-width: 650px) {
        .title-padding {
            padding-left: 5vw;
        }
    }

    .caption {
        font-size: 10pt;
    }

    .resource-separators {
        padding-bottom: 15px;;
    }

</style>
