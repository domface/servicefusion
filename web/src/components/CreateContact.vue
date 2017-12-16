<template>
  <el-row align="middle">
    <el-col>
      <el-card class="box-card" style="height: 94vh; overflow: scroll">

        <div slot="header" class="clearfix">
          <el-button @click="cancel" style="float: left; padding: 8px 7px" type="danger">Cancel</el-button>
          <span>New Contact</span>
          <el-button  v-if="!submitted" @click="submitForm('person')" style="float: right; padding: 8px 7px" type="success">Create</el-button>
          <el-button v-if="submitted" style="float: right; padding: 8px 7px" type="success" :loading="true" ></el-button>
        </div>
        <el-form :status-icon="true"
                 label-position="top"
                 ref="person"
                 :model="person"
                 label-width="80px">
          <div class="text item">
            <el-row type="flex" class="section_heading">
              <el-col :span="12" style="text-align: left">
                <div>Personal Info</div>

              </el-col>


            </el-row>

            <el-row :gutter="16" justify="space-between">
              <el-col :span="8">
                <el-form-item label="First Name"
                              :rules="{required: true, message: 'Please Enter a First Name', trigger: 'blur'}"
                              prop="first_name">
                  <el-input placeholder="First Name" v-model="person.first_name"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <el-form-item label="Last Name"
                              :rules="{required: true, message: 'Please Enter a Last Name', trigger: 'blur'}"
                              prop="last_name">
                  <el-input placeholder="Last Name" v-model="person.last_name"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="8">
                <div class="">
                  <el-form-item label="Birthday"
                                :rules="{ pattern:/^\d{4}-\d{2}-\d{2}$/, required: true, message: 'Please add a birthday', trigger: 'blur'}"
                                prop="date_of_birth">
                    <el-date-picker

                      v-model="person.date_of_birth"
                      type="date"
                      placeholder="Birth Date"
                      value-format="yyyy-MM-dd">
                    </el-date-picker>
                  </el-form-item>
                </div>
              </el-col>
            </el-row>
          </div>




          <!--   ADDRESSES   --->




          <el-row type="flex" class="section_heading">
            <el-col :span="6" style="text-align: left">
              <div>Addresses</div>
            </el-col>
            <el-col :span="18" style="text-align: right">

              <el-tooltip class="item" effect="light" content="Add Address" placement="top-start">
                <el-button class="button-pad" size="mini" type="success" icon="el-icon-plus"
                           @click="addAddress"></el-button>
              </el-tooltip>
            </el-col>
          </el-row>
          <p v-if="person.addresses.length === 0">No Address</p>
          <el-row class="address-divider" v-for="(address, index) in person.addresses" :gutter="16"
                  justify="space-between">





            <el-col :span="12">


              <el-form-item label="Street"
                            :prop="'addresses.' + index + '.street'"
                            :rules="{required: true, message: 'Please Enter a Street Name', trigger: 'blur'}">

                <el-input placeholder="Street Name" v-model="address.street"></el-input>
              </el-form-item>
              <el-form-item label="Apartment / Suite" prop="street_2">
                <el-input placeholder="Apartment / Suite" v-model="address.street_2"></el-input>
              </el-form-item>


            </el-col>
            <el-col :span="12">


              <el-form-item label="City"
                            :prop="'addresses.' + index + '.city'"
                            :rules="{required: true, message: 'Please Enter a City', trigger: 'blur'}">
                <el-input placeholder="City" v-model="address.city"></el-input>
              </el-form-item>


              <el-row :gutter="8" justify="space-between">
                <el-col :span="12">


                  <el-form-item label="State"
                                :prop="'addresses.' + index + '.state'"
                                :rules="{required: true, message: 'Please Enter a State', trigger: 'blur'}">
                    <el-select v-model="address.state" placeholder="State">
                      <el-option v-for="state in states" :label="state[1]" :value="state[0]"></el-option>
                    </el-select>
                  </el-form-item>


                </el-col>
                <el-col :span="12">


                  <el-form-item label="Zip Code"
                                :rules="{required: true, pattern:/(^\d{5}$)|(^\d{5}-\d{4}$)/, message: 'Please Enter a Valid Zip', trigger: 'blur'}"
                                :prop="'addresses.' + index + '.zip'">
                    <el-input placeholder="Zip Code" v-model="address.zip"></el-input>
                  </el-form-item>


                </el-col>
              </el-row>
            </el-col>

          </el-row>


          <el-row type="flex" class="section_heading">
            <el-col :span="6" style="text-align: left">
              <div>Phone Numbers</div>
            </el-col>
            <el-col :span="18" style="text-align: right">
              <el-tooltip class="item" effect="light" content="Add Phone Number" placement="top-start">
                <el-button class="button-pad" size="mini" type="success" icon="el-icon-plus"
                           @click="addPhoneNumber"></el-button>
              </el-tooltip>
            </el-col>
          </el-row>


          <el-row v-for="(phone, index) in person.phone_numbers" :gutter="16" justify="space-between">
            <el-col :span="4">
              <el-form-item label="Type"
                            :rules="{required: true, message: 'Please Enter a Phone Type', trigger: 'blur'}"
                            :prop="'phone_numbers.' + index + '.type'">
              <el-select v-model="phone.type" placeholder="Type">
                <el-option label="Cell" value="cell"></el-option>
                <el-option label="Home" value="home"></el-option>
                <el-option label="Work" value="work"></el-option>
              </el-select>
                </el-form-item>
            </el-col>
            <el-col :span="20">
              <el-form-item label="Number"
                            :rules="{required: true, pattern:/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im, message: 'Please Enter a Valid Phone Number', trigger: 'blur'}"
                            :prop="'phone_numbers.' + index + '.number'">
              <el-input placeholder="Phone Number" v-model="phone.number"></el-input>
                </el-form-item>
            </el-col>
          </el-row>


          <el-row type="flex" class="section_heading">
            <el-col :span="6" style="text-align: left">
              <div>Emails</div>
            </el-col>
            <el-col :span="18" style="text-align: right">
              <el-tooltip class="item" effect="light" content="Add Email" placement="top-start">
                <el-button class="button-pad" size="mini" type="success" icon="el-icon-plus"
                           @click="addEmail"></el-button>
              </el-tooltip>
            </el-col>
          </el-row>

          <el-row v-for="(email, index) in person.emails" :gutter="16" justify="space-between">
            <el-col :span="24">
              <el-form-item
                :prop="'emails.' + index + '.email'"
                label="Email"
                :rules="[
      { required: true, message: 'Please input email address', trigger: 'blur' },
      { type: 'email', message: 'Please input correct email address', trigger: 'blur,change' }
    ]">
              <el-input placeholder="Please Enter an Email" v-model="email.email"></el-input>
                </el-form-item>
            </el-col>
          </el-row>


        </el-form>
      </el-card>
    </el-col>

  </el-row>

</template>

<script type="text/babel">
  import axios from 'axios'
  const api_url = 'http://sf.jawn.it/api/'
  export default {
    name: 'create-contact',
    data () {
      return {
        person: {
          first_name: "",
          last_name: "",
          date_of_birth: "",
          addresses: [],
          phone_numbers: [{
            key: 1,
            number: null,
            type: ""
          }],
          emails: [{
            key: 1,
            email: ""
          }]
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
        submitted: false
      }
    },
    methods: {
      createResource(resource) {
        axios.post(api_url + resource + "/", this.person)
          .then(response => {
            this.$router.push({path: '/'})
        this.$message({
          type: 'success',
          message: 'Contact Saved'
        })
      })
      .catch(e => {
        this.submitted = false
        this.$message({
          type: 'danger',
          message: 'Error'
        });
      })

      },
      addPhoneNumber() {
        this.person.phone_numbers.push(
          {
            key: Date.now(),
            number: null,
            type: ""
          }
        )
      },
      addAddress() {
        this.person.addresses.push(
          {
            key: Date.now(),
            street: "",
            street_2: "",
            city: "",
            state: "",
            zip: null
          }
        )

      },
      addEmail() {
        this.person.emails.push(
          {
            key: Date.now(),
            email: ""
          }
        )
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.submitted = true
            this.createResource('add_person')
          } else {
            return false;
          }
      });
      },
      save() {

      },
      cancel() {
        this.$confirm('Your changes will be lost. Continue?', 'Warning', {
          confirmButtonText: 'OK',
          cancelButtonText: 'Cancel',
          type: 'warning',
          center: true
        }).then(() => {
          this.$router.push({path: '/'})
        this.$message({
          type: 'warning',
          message: 'Contact not Saved'
        });
      }).
        catch(() => {
          this.$message({
          type: 'info',
          message: 'Canceled'
        });
      })
        ;
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
    font-size: 15pt;

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
    margin-bottom: 3px;
  }

  .el-input.is-disabled .el-input__inner {
    background-color: #ffffff;
    border-color: #ffffff;
    color: #4d5057;
    cursor: default;
  }

  .el-main {
    padding: 0px;
  }

  .el-aside {
    padding-top: 3vh;
    padding-bottom: 3vh;
    padding-left: 3vh;
    padding-right: 0vh;
    min-width: 350px;
  }

  .el-form-item__label {
    height: 30px;
  }
</style>
