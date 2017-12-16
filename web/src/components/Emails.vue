<template>


    <el-form :status-icon="true" ref="email" :model="form" label-width="100px">

        <el-row class="section_heading">
            <el-col :span="6" style="text-align: left">
                <div>Emails</div>
            </el-col>
            <el-col :span="18" style="text-align: right">
                <el-tooltip class="item" effect="light" content="Add Email" placement="left-start">
                    <el-button v-if="!add"
                               class="button-pad success"
                               size="medium"
                               type="text"
                               icon="el-icon-circle-plus "
                               @click="addNewResource()"></el-button>
                </el-tooltip>
                <el-button-group v-if="add">
                    <el-button class="button-pad danger"
                               type="text"
                               @click="cancelAdd('email')"
                               icon="el-icon-error"
                    ></el-button>
                    <el-button type="text"
                               class="button-pad success"
                               icon="el-icon-success"
                               @click="save('email', form.emails)"></el-button>

                </el-button-group>
            </el-col>


        </el-row>


        <!--   EMAILS   --->


        <el-row v-for="(email, index) in this.form.emails" :gutter="26" justify="space-around" align="middle"
                type="flex">


            <el-col class="resource-separators" type="flex" v-if="!form.emails[index].edit">
                <el-row :gutter="56" class="title-padding" type="flex" justify="middle" align="middle">

                    <el-col :span="4" style="text-align: left">

                        <a :href="'mailto:' + email.email">
                            <el-tag type="info">email</el-tag>
                        </a>

                    </el-col>
                    <el-col style="text-align: left">{{ email.email }}</el-col>
                </el-row>

            </el-col>


            <el-col class="resource-separators" v-if="form.emails[index].edit" :span="20">
                <el-form-item
                        :prop="'emails.' + index + '.email'"
                        label="Email"
                        :rules="[
      { required: true, message: 'Please input email email', trigger: 'blur' },
      { type: 'email', message: 'Please input correct email email', trigger: 'blur,change' }
    ]">
                    <el-input placeholder="Please Enter an Email"
                              :disabled="!email.edit"
                              v-model="email.email"></el-input>
                </el-form-item>
            </el-col>

            <el-col class="resource-separators" :span="2" style="text-align: right">
                    <el-button-group v-if="!form.emails[index].edit && !add">
                        <el-tooltip class="item" effect="light" content="Edit Email" placement="left-start">
                            <el-button class="button-pad"
                                       size="medium"
                                       type="text"
                                       icon="el-icon-edit"
                                       @click="editOn(index)">

                            </el-button>
                        </el-tooltip>
                        <el-tooltip class="item" effect="light" content="Delete Email"
                                    placement="left-start">
                            <el-button class="button-pad danger"
                                       @click="del('email', email)"
                                       type="text"
                                       icon="el-icon-delete">
                            </el-button>
                        </el-tooltip>
                    </el-button-group>
                    </el-tooltip>
                    <el-button-group v-if="form.emails[index].edit && !add">
                        <el-button class="button-pad danger"
                                   type="text"
                                   icon="el-icon-error"
                                   @click="editOff(index)"
                        ></el-button>
                        <el-button type="text"
                                   class="button-pad success"
                                   icon="el-icon-success"
                                   @click="update('email', email, index)"></el-button>

                    </el-button-group>

                </el-col>


        </el-row>

    </el-form>


</template>

<script type="text/babel">

    export default {

        name: 'emails',
        props: ['person', 'emails', 'pluralize', 'updateResource', 'createResource', 'updateUi', 'deleteResource'],
        components: {},
        methods: {
            update(resource, data, index) {
                this.$refs['email'].validate((valid) => {
                    if (valid) {

                        let r_plural = this.pluralize(resource)
                        this.updateResource(r_plural, data)
                                .then(response => {
                                    this.editOff(index)
                                    this.updateUi()
                                    this.$message({
                                        type: 'success',
                                        message: 'Contact Updated'
                                    })
                                })
                                .catch(e => {
                                    this.editOff(index)
                                    this.updateUi()
                                    this.$message({
                                        type: 'danger',
                                        message: 'Error'
                                    })
                                })


                    }
                    else {
                        return false;
                    }

                })

            },
            save(resource, data) {
                this.$refs['email'].validate((valid) => {
                    if (valid) {

                        let r_plural = this.pluralize(resource)
                        let new_data = data.slice(-1)[0]
                        new_data['person_id'] = this.person
                        let index = data.length - 1
                        this.createResource(r_plural, new_data)
                                .then(response => {
                                    this.$message({
                                        type: 'success',
                                        message: 'Contact Saved'
                                    })
                                    this.add = false
                                    this.editOff(index);
                                    this.updateUi()
                                })
                                .catch(e => {
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
            del(resource, data) {
                    if (this.form.emails.length < 2) {
                        this.$alert('You must have at least one ' + resource.replace('_', ' ') + ' for each contact.', 'Error', {
                            confirmButtonText: 'OK'

                        });
                        return false;
                    }
                    else {

                        this.$confirm('This will permanently delete it. Continue?', 'Warning', {
                            confirmButtonText: 'OK',
                            cancelButtonText: 'Cancel',
                            type: 'warning',
                            center: true
                        }).then(() => {
                            let r_plural = this.pluralize(resource)
                            this.deleteResource(r_plural, data.id)
                            this.$message({
                                type: 'success',
                                message: 'Delete completed'
                            });
                        }).catch((e) => {
                            alert(e);
                            this.$message({
                                type: 'info',
                                message: 'Delete canceled'
                            });
                        });
                    }


            },
            addNewResource() {
                this.form.emails.push({
                    email: "",
                    edit: true
                })
                this.add = true
            },
            cancelAdd(){
                this.form.emails.pop()
                this.add = false
            },
            editOn(index) {
                this.$set(this.form.emails[index], "edit", true)
                this.form.emails[index].edit = true
                this.form.emails.push(null)
                this.form.emails.pop()

            },
            editOff(index) {
                this.$set(this.form.emails[index], "edit", false)
                this.form.emails[index].edit = false
                this.form.emails.push(null)
                this.form.emails.pop()

            },
            init() {
                this.form.emails = [];
                if (this.emails) {
                    for (let email of this.emails) {
                        email['edit'] = false
                        this.form.emails.push(email)
                    }
                }
            }
        },
        data () {
            return {
                edit: [],
                add: false,
                form: {
                    person: this.person,
                    emails: []
                }
            }
        },
        created() {
            this.init()
        },

        watch: {
            'emails' (to, from) {
                this.init()
            }
        }
    }

</script>


