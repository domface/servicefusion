<template>


    <el-form :status-icon="true" ref="address" :model="form" label-width="100px">

        <el-row class="section_heading">
            <el-col :span="6" style="text-align: left">
                <div>Addresses</div>
            </el-col>
            <el-col :span="18" style="text-align: right">
                <el-tooltip class="item" effect="light" content="Add Address" placement="left-start">
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
                               @click="cancelAdd()"
                    ></el-button>
                    <el-button type="text"
                               class="button-pad success"
                               icon="el-icon-success"
                               @click="save('address', form.addresses)"></el-button>

                </el-button-group>
            </el-col>
        </el-row>


        <el-row class="address-divider" v-for="(address, index) in this.form.addresses"
                :gutter="26"
                type="flex"
                justify="space-around" align="middle">


            <el-col class="resource-separators" type="flex" v-if="!form.addresses[index].edit">
                <el-row  class="title-padding" type="flex" justify="middle" align="middle">

                    <el-col :span="4" style="text-align: left">

                        <a target="_blank" :href="'https://maps.google.com/?q=' + address.street + ' ' + address.street_2 + ' ' + address.city + ' ' + address.state + ' ' + address.zip"><el-tag>map</el-tag></a>

                    </el-col>
                    <el-col :xs="18" :sm="18" v-if="!form.addresses[index].edit">
                        <el-row  type="flex" justify="middle" align="middle">

                            <el-col style="text-align: left">

                                {{ address.street }} {{ address.street_2 }}

                            </el-col>
                        </el-row>

                        <el-row type="flex" justify="start">

                            <el-col style="text-align: left">
                                <div>
                                    {{ address.city }} {{ address.state }} {{ address.zip }}
                                </div>
                            </el-col>
                        </el-row>
                    </el-col>
                </el-row>

            </el-col>





            <!--   STREET   --->

            <el-col v-if="form.addresses[index].edit">
                <el-form-item label="Street"
                              :prop="'addresses.' + index + '.street'"
                              :rules="{required: true, message: 'Please Enter a Street Name', trigger: 'blur'}">

                    <el-input placeholder="Street Name"
                              v-model="address.street"></el-input>
                </el-form-item>
                <el-form-item prop="street_2">
                    <el-input placeholder="Apartment / Suite"
                              v-model="address.street_2"></el-input>
                </el-form-item>


                <!--   CITY STATE ZIP   --->


                <el-form-item label="City"
                              :prop="'addresses.' + index + '.city'"
                              :rules="{required: true, message: 'Please Enter a City', trigger: 'blur'}">
                    <el-input placeholder="City"
                              v-model="address.city"></el-input>
                </el-form-item>


                <el-row :gutter="16" justify="space-between">
                    <el-col :span="8">


                        <el-form-item label="State"
                                      :prop="'addresses.' + index + '.state'"
                                      :rules="{required: true, message: 'Please Enter a State', trigger: 'blur'}">
                            <el-select v-model="address.state"
                                       placeholder="State">
                                <el-option v-for="state in states" :label="state[0]"
                                           :value="state[0]"></el-option>
                            </el-select>
                        </el-form-item>


                    </el-col>
                    <el-col :span="16">
                        <el-form-item label="Zip Code"
                                      :rules="{required: true, pattern:/(^\d{5}$)|(^\d{5}-\d{4}$)/, message: 'Please Enter a Valid Zip', trigger: 'blur'}"
                                      :prop="'addresses.' + index + '.zip'">
                            <el-input placeholder="Zip Code"
                                      v-model="address.zip"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-col>


                <el-col :span="2" style="text-align: right">

                    <el-button-group v-if="!form.addresses[index].edit && !add && !edit">
                        <el-tooltip class="item" effect="light" content="Edit Address"
                                    placement="left-start">
                            <el-button v-if="!form.addresses[index].edit"
                                       class="button-pad"
                                       size="medium"
                                       type="text"
                                       icon="el-icon-edit"
                                       @click="editOn(index)">

                            </el-button>
                        </el-tooltip>
                        <el-tooltip class="item" effect="light" content="Delete Address"
                                    placement="left-start">
                            <el-button class="button-pad danger"
                                       @click="del('address', address)"
                                       type="text"
                                       icon="el-icon-delete">
                            </el-button>
                        </el-tooltip>
                    </el-button-group>
                    </el-tooltip>
                    <el-button-group v-if="form.addresses[index].edit && !add">
                        <el-button class="button-pad danger"
                                   type="text"
                                   icon="el-icon-error"
                                   @click="editOff(index)"
                        ></el-button>
                        <el-button type="text"
                                   class="button-pad success"
                                   icon="el-icon-success"
                                   @click="update('address', address, index)"></el-button>

                    </el-button-group>

                </el-col>



        </el-row>

    </el-form>

</template>


<script type="text/babel">

    export default {

        name: 'addresses',
        props: ['person', 'addresses', 'pluralize', 'updateResource', 'createResource', 'updateUi', 'deleteResource'],
        components: {},
        methods: {
            update(resource, data, index) {
                this.$refs['address'].validate((valid) => {
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
                this.$refs['address'].validate((valid) => {
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
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: 'Delete canceled'
                    });
                });
            },
            addNewResource() {
                this.form.addresses.push({
                    person_id: this.person,
                    street: "",
                    street_2: "",
                    city: "",
                    state: "",
                    zip: "",
                    edit: true
                })
                this.add = true
            },
            cancelAdd(){
                this.form.addresses.pop()
                this.add = false
            },
            editOn(index) {
                this.$set(this.form.addresses[index], "edit", true)
                this.form.addresses[index].edit = true
                this.edit = true;
                this.form.addresses.push(null)
                this.form.addresses.pop()

            },
            editOff(index) {
                this.$set(this.form.addresses[index], "edit", false)
                this.form.addresses[index].edit = false
                this.edit = false;
                this.form.addresses.push(null)
                this.form.addresses.pop()

            },
            init() {
                this.form.addresses = [];
                if (this.addresses) {
                    for (let address of this.addresses) {
                        address['edit'] = false;
                        address['person_id'] = this.person;
                        this.form.addresses.push(address)
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
                    addresses: []
                },
                states: [['AL', 'Alabama'], ['AZ', 'Arizona'], ['AR', 'Arkansas'], ['CA', 'California'], ['CO', 'Colorado'],
                    ['CT', 'Connecticut'], ['DE', 'Delaware'], ['DC', 'District of Columbia'], ['FL', 'Florida'],
                    ['GA', 'Georgia'], ['ID', 'Idaho'], ['IL', 'Illinois'], ['IN', 'Indiana'], ['IA', 'Iowa'],
                    ['KS', 'Kansas'], ['KY', 'Kentucky'], ['LA', 'Louisiana'], ['ME', 'Maine'], ['MD', 'Maryland'],
                    ['MA', 'Massachusetts'], ['MI', 'Michigan'], ['MN', 'Minnesota'], ['MS', 'Mississippi'],
                    ['MO', 'Missouri'], ['MT', 'Montana'], ['NE', 'Nebraska'], ['NV', 'Nevada'], ['NH', 'New Hampshire'],
                    ['NJ', 'New Jersey'], ['NM', 'New Mexico'], ['NY', 'New York'], ['NC', 'North Carolina'],
                    ['ND', 'North Dakota'], ['OH', 'Ohio'], ['OK', 'Oklahoma'], ['OR', 'Oregon'], ['PA', 'Pennsylvania'],
                    ['RI', 'Rhode Island'], ['SC', 'South Carolina'], ['SD', 'South Dakota'], ['TN', 'Tennessee'],
                    ['TX', 'Texas'], ['UT', 'Utah'], ['VT', 'Vermont'], ['VA', 'Virginia'], ['WA', 'Washington'],
                    ['WV', 'West Virginia'], ['WI', 'Wisconsin'], ['WY', 'Wyoming']],
            }
        },
        created() {
            this.init()
        },
        watch: {
            'addresses' (to, from) {
                this.init()
            }
        }
    }

</script>