<template>
<div class="has-background-primary pb-6">
  <section class="container py-6">
    <div class="columns is-multiline">
      <div class="column is-8 is-offset-2 register">
        <div class="columns">
          <div class="column has-text-left">
            <router-link :to="{ name: 'LandingPage' }" class="button is-rounded is-primary is-inverted is-pulled-right"><strong>
                Regresar</strong>
            </router-link>
            <div class="card p-5 mt-6">
              <h1 class="title is-4 has-text-centered">Registro</h1>
              <p class="description pb-5">Ingresa tu información para registrar al evento seleccionado</p>
              <form @submit="Submit">
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Nombres y Apellidos</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <p class="control is-expanded has-icons-left">
                        <input class="input" type="text" placeholder="Nombres" v-bind:class="{ 'is-danger': exeptions.name }" v-model="form_visitor.name">
                      <p class="help is-danger">{{exeptions.name}}</p>
                      </p>
                    </div>
                    <div class="field">
                      <p class="control is-expanded has-icons-left has-icons-right">
                        <input class="input" type="text" placeholder="Apellidos" v-bind:class="{ 'is-danger': exeptions.last_name }"  v-model="form_visitor.last_name">
                      <p class="help is-danger">{{exeptions.last_name}}</p>
                      </p>
                    </div>
                  </div>
                </div>

                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Documento</label>
                  </div>
                  <div class="field-body">
                    <div class="field is-narrow">
                      <div class="control">
                        <div class="select is-fullwidth" v-bind:class="{ 'is-danger': exeptions.document_type }">
                          <select v-model="form_visitor.document_type">
                            <option :value="null" disabled>Tipo de documento</option>
                            <option v-for="option in document_options" v-bind:value="option.value">{{option.text}}</option>
                          </select>

                          <p class="help is-danger">{{exeptions.document_type}}</p>
                        </div>
                      </div>
                    </div>
                    <div class="field">
                      <p class="control is-expanded has-icons-left has-icons-right">
                        <input class="input" type="text" placeholder="Número de documento" v-bind:class="{ 'is-danger': exeptions.document_id }" v-model="form_visitor.document_id">
                      <p class="help is-danger">{{exeptions.document_id}}</p>
                      </p>
                    </div>
                  </div>
                </div>

                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Ciudad de origen</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <input class="input" type="text" placeholder="Ingrese ciudad de origen" v-bind:class="{ 'is-danger': exeptions.city }" v-model="form_visitor.city">
                        <p class="help is-danger">{{exeptions.city}}</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Empresa</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <input class="input" type="text" placeholder="Ingrese nombre de la empresa" v-model="form_visitor.company_name">
                      </div>
                    </div>
                  </div>
                </div>

                <hr>
                <button type="submit" class="button is-block is-primary is-fullwidth is-medium is-rounded">Registrar</button>
              </form>
            </div>

          </div>
        </div>
      </div>
    </div>
  </section>
</div>
</template>


<script>
import axios from 'axios';

import swal from 'sweetalert';

export default {
  name: "",
  data: () => ({
    form_visitor: {
      name: null,
      last_name: null,
      document_type: null,
      document_id: null,
      city: null,
      company_name: null,
      event: null,
    },
    document_options: [{
        text: 'Tarjeta de identidad',
        value: 'TI'
      },
      {
        text: 'Cédula de ciudadania',
        value: 'CC'
      },
      {
        text: 'Cédula extranjera',
        value: 'CE'
      },
    ],
    exeptions: {
      name: '',
      last_name: '',
      document_type: '',
      document_id: '',
      city: '',
    }
  }),
  methods: {
    GetEvent() {
      const path = `http://127.0.0.1:8000/api/v1.0/events/${this.$route.params.event_id}/`;
      axios.get(path).then((response) => {
        this.form_visitor.event = response.data.id;
      })
    },
    Submit(e) {
      e.preventDefault();
      const path = "http://127.0.0.1:8000/api/v1.0/visitors/";
      axios.post(path, this.form_visitor).then(() => {
          swal({
            title: 'Éxito!',
            text: 'Se ha registrado al evento',
            icon: 'success',
            button: false
          });
          setTimeout('document.location.assign("http://127.0.0.1:8080/")', 1200);
        })
        .catch((error) => {
          // debugger
          this.exeptions = {
            name: '',
            last_name: '',
            document_type: '',
            document_id: '',
            city: '',
          }
          if (error.response.data.name) {
            const ex_name = error.response.data.name
            ex_name.forEach((expt) => {
              this.exeptions.name = expt;
            });
          }
          if (error.response.data.last_name) {
            const ex_last_name = error.response.data.last_name
            ex_last_name.forEach((expt) => {
              this.exeptions.last_name = expt;
            });
          }
          if (error.response.data.document_type) {
            const ex_document_type = error.response.data.document_type
            ex_document_type.forEach((expt) => {
              this.exeptions.document_type = expt;
            });
          }
          if (error.response.data.document_id) {
            const ex_document_id = error.response.data.document_id
            ex_document_id.forEach((expt) => {
              this.exeptions.document_id = expt;
            });
          }
          if (error.response.data.city) {
            const ex_city = error.response.data.city
            ex_city.forEach((expt) => {
              this.exeptions.city = expt;
            });
          }
        })
    }
  },
  created() {
    this.GetEvent();
  }
}
</script>
<style lang="scss" scoped>
</style>
