<template>


    <el-form :status-icon="true" ref="form" :model="form" label-width="100px">
        <el-row class="section_heading">
            <el-col :span="6" style="text-align: left">
                <div>Phone Numbers</div>
            </el-col>
            <el-col :span="18" style="text-align: right">
                <el-tooltip class="item" effect="light" content="Add Phone Number" placement="left-start">
                    <el-button v-if="!add && !edit"
                               class="button-pad success"
                               size="medium"
                               type="text"
                               icon="el-icon-circle-plus "
                               @click="addNewResource()"></el-button>
                </el-tooltip>
                <el-button-group v-if="add">
                    <el-button class="button-pad danger"
                               type="text"
                               icon="el-icon-error"
                               @click="cancelAdd('phone_number')"
                    ></el-button>
                    <el-button type="text"
                               class="button-pad success"
                               icon="el-icon-success"
                               @click="save('phone_number', numbers)"></el-button>

                </el-button-group>
            </el-col>
        </el-row>


        <!--   PHONE NUMBERS   --->


        <el-row v-for="(number, index) in this.form.numbers"
                :gutter="16"
                type="flex"
                justify="space-between"
                align="middle">


            <el-col class="resource-separators" type="flex" v-if="!form.numbers[index].edit">
                <el-row class="title-padding" type="flex" justify="middle" align="middle">

                    <el-col :span="4" style="text-align: left">

                        <a :href="'tel:' + number.number.toString()"><el-tag v-if="number.type === 'cell'">{{ number.type }}</el-tag><el-tag type="warning" v-if="number.type === 'work'">{{ number.type }}</el-tag><el-tag type="success" v-if="number.type === 'home'">{{ number.type }}</el-tag></a>

                    </el-col>
                    <el-col style="text-align: left">{{ number.number | phone }}</el-col>
                </el-row>

            </el-col>

            <el-col class="resource-separators" v-if="form.numbers[index].edit">
                <el-col  :span="8">
                    <el-form-item label="Type"
                                  :rules="{required: true, message: 'Please Enter a Phone Type', trigger: 'blur'}"
                                  :prop="'numbers.' + index + '.type'">
                        <el-select v-model="number.type"
                                   :disabled="!number.edit"
                                   placeholder="Type">
                            <el-option label="Cell" value="cell"></el-option>
                            <el-option label="Home" value="home"></el-option>
                            <el-option label="Work" value="work"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="14">
                    <el-form-item label="Number"
                                  :rules="{required: true, pattern:/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im, message: 'Please Enter a Valid Phone Number', trigger: 'blur'}"
                                  :prop="'numbers.' + index + '.number'">
                        <el-input placeholder="Phone Number"
                                  :disabled="!number.edit"
                                  v-model="number.number"></el-input>
                    </el-form-item>
                </el-col>
            </el-col>

                <el-col class="resource-separators" :span="2" style="text-align: right">
                    <el-button-group v-if="!form.numbers[index].edit && !add && !edit">
                        <el-tooltip class="item" effect="light" content="Edit Address"
                                    placement="left-start">
                            <el-button class="button-pad"
                                       size="medium"
                                       type="text"
                                       icon="el-icon-edit"
                                       @click="editOn(index)">

                            </el-button>
                        </el-tooltip>
                        <el-tooltip class="item" effect="light" content="Delete Address"
                                    placement="left-start">
                            <el-button class="button-pad danger"
                                       @click="del('phone_number', number, index)"
                                       type="text"
                                       icon="el-icon-delete">
                            </el-button>
                        </el-tooltip>
                    </el-button-group>
                    </el-tooltip>
                    <el-button-group v-if="form.numbers[index].edit && !add">
                        <el-button class="button-pad danger"
                                   type="text"
                                   icon="el-icon-error"
                                   @click="editOff(index)"
                        ></el-button>
                        <el-button type="text"
                                   class="button-pad success"
                                   icon="el-icon-success"
                                   @click="update('phone_number', number, index)"></el-button>

                    </el-button-group>

                </el-col>

        </el-row>
    </el-form>

</template>

<script type="text/babel">

    export default {

        name: 'phone-numbers',
        props: ['person', 'numbers', 'pluralize', 'updateResource', 'createResource', 'updateUi', 'deleteResource'],
        components: {},
        methods: {
            update(resource, data, index) {
                this.$refs['form'].validate((valid) => {
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
                this.$refs['form'].validate((valid) => {
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
                if (this.form.numbers.length < 2) {
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
                this.add = true;
                this.form.numbers.push({
                    person: this.person,
                    type: null,
                    number: "",
                    edit: true
                });

            },
            cancelAdd(){
                this.form.numbers.pop()
                this.add = false
            },
            editOn(index) {
                this.$set(this.form.numbers[index], "edit", true)
                this.form.numbers[index].edit = true
                this.edit = true;
                this.form.numbers.push(null)
                this.form.numbers.pop()

            },
            editOff(index) {
                this.$set(this.form.numbers[index], "edit", false)
                this.form.numbers[index].edit = false
                this.edit = false;
                this.form.numbers.push(null)
                this.form.numbers.pop()

            },
            init() {
                this.form.numbers = [];
                if (this.numbers) {
                    for (let number of this.numbers) {
                        number['edit'] = false
                        this.form.numbers.push(number)
                    }
                }
            }
        },
        data () {
            return {
                edit: false,
                add: false,
                form: {
                    person: this.person,
                    numbers: [],
                    updater: []
                },
            }
        },
        created() {
            this.init()
        },

        watch: {
            'numbers' (to, from) {
                this.init()
            }
        }
    }

</script>
