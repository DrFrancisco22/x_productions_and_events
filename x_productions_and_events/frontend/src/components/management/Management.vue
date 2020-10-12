<template>
<div class="has-background-white-ter">
  <!-- Importar componente Navbar -->
  <Navbar />

  <div class="container pt-5">
    <div class="columns">
      <div class="column">
          <h1 class="title has-text-left">Panel de administración</h1>
        <section class="info-tiles">
          <div class="tile is-ancestor has-text-centered">
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title">{{counters.n_events}}</p>
                <p class="subtitle">Eventos registrados</p>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title">{{counters.n_visitors}}</p>
                <p class="subtitle">Visitantes registrados</p>
              </article>
            </div>
          </div>
        </section>
        <div class="columns">
          <div class="column is-4">
            <div class="card">
              <form @submit="Submit">
                <header class="card-header">

                  <!-- validación para verificar si se está editando un eveto -->
                  <p v-if="event_obj.id" class="card-header-title">
                    Editar evento
                  </p>
                  <p v-else class="card-header-title">
                    Agregar evento
                  </p>
                  <!-- fin de validación -->
                  <button type="button" class="button is-primary is-small my-2 mr-2 is-outlined is-pulled-right" v-on:click="CleanForm()">
                    Limpiar
                  </button>

                </header>
                <div class="card-content">
                  <div class="content has-text-left">
                    <div class="field">
                      <label for="name" class="label">Nombre</label>
                      <div class="control">
                        <input type="text" class="input" v-bind:class="{ 'is-danger': exeptions.name}" name="name" v-model="event_obj.name">
                        <p class="help is-danger">{{exeptions.name}}</p>
                      </div>

                    </div>
                    <div class="field">
                      <label for="datetime" class="label">Fecha y hora</label>
                      <div class="control">
                        <date-picker v-model="event_obj.date_time" type="datetime" format="YYYY-MM-DD hh:mm: A" input-class="input" :editable="false" name="date_time"></date-picker>
                        <p class="help is-danger">{{exeptions.date_time}}</p>
                      </div>

                    </div>
                    <div class="field">
                      <label for="place" class="label">Lugar</label>
                      <div class="control">
                        <input type="text" class="input" name="place" v-bind:class="{ 'is-danger': exeptions.place }" v-model="event_obj.place">
                        <p class="help is-danger">{{exeptions.place}}</p>
                      </div>

                    </div>
                  </div>
                </div>
                <footer class="card-footer">
                  <button type="submit" name="button" class="button is-success is-fullwidth">Guardar</button>
                </footer>

              </form>
            </div>
          </div>

          <div class="column is-8">
            <div class="card events-card">
              <header class="card-header">
                <p class="card-header-title">
                  Eventos
                </p>
              </header>


              <div v-if="event_list.length !== 0 ">
                <table class="table is-striped is-narrow is-hoverable is-fullwidth has-text-left">
                  <th class="p-4" v-for="item in table_header">{{item}}</th>
                  </thead>
                  <tbody>
                    <tr v-for="event in event_list">
                      <!-- <td width="5%"><i class="fa fa-bell-o"></i></td> -->
                      <td class="pl-4">{{event.name}}</td>
                      <td class="pl-4">{{event.date_time}}</td>
                      <td class="pl-4">{{event.place}}</td>
                      <td class="level-right py-auto py-5 pr-4">
                        <router-link :to="{ name: 'VisitorList', params: { event_id: event.id }}" class="button is-small is-primary mx-1  is-rounded">Ver</router-link>
                        <a class="button is-small is-link mx-1 is-rounded" v-on:click="EventEdit(event)">Editar</a>
                        <a class="button is-small is-danger mx-1  is-rounded" v-on:click="EventDelete(event.id)">Borrar</a>
                      </td>
                    </tr>
                  </tbody>
                </table>

              </div>
              <div v-else class="notification is-warning m-3">
                <p>No hay eventos registrados</p>
              </div>

              <!-- <footer class="card-footer">
                <a href="#" class="card-footer-item">View All</a>
              </footer> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>
</template>
<script>
import axios from 'axios';
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';

import Navbar from '@/components/management/Navbar'

import {
  Notyf
} from 'notyf';
import 'notyf/notyf.min.css';

import swal from 'sweetalert';

const noty = new Notyf({
  duration: 4000,
  position: {
    x: 'right',
    y: 'top',
  },
});

export default {
  // name: "events",
  components: {
    DatePicker,
    Navbar
  },
  data: () => ({
    event_obj: {
      id: null,
      name: null,
      date_time: null,
      place: null
    },
    event_list: [],
    table_header: ['Nombre', 'Fecha y hora', 'Lugar', ''],
    event_delete: null,
    counters: {
      n_events: null,
      n_visitors: null,
    },
    exeptions: {
      name: '',
      date_time: null,
      place: '',
    }
  }),
  methods: {
    EventList() {
      const path = "http://127.0.0.1:8000/api/v1.0/events/";
      axios.get(path).then((response) => {
          this.event_list = response.data
        })
        .catch((error) => {
          const noty = new Notyf();
          noty.error(error);
        })
    },
    EventEdit(event) {
      this.event_obj.id = event.id;
      this.event_obj.name = event.name;
      this.event_obj.date_time = new Date(event.date_time);
      this.event_obj.place = event.place;
    },
    Submit(e) {
      e.preventDefault();
      if (this.event_obj.id) {
        const path = `http://127.0.0.1:8000/api/v1.0/events/${this.event_obj.id}/`;
        axios.put(path, this.event_obj).then((response) => {
            swal({
              title: 'Éxito!',
              text: 'Evento actualizado con éxito',
              icon: 'success',
              button: false
            });
            setTimeout('document.location.reload()', 1000);
          })
          .catch((error) => {
            this.ExeptionControl(error);
          })
      } else {
        const path = "http://127.0.0.1:8000/api/v1.0/events/";
        axios.post(path, this.event_obj).then((response) => {
            swal({
              title: 'Éxito!',
              text: 'Evento creado con éxito',
              icon: 'success',
              button: false
            });
            setTimeout('document.location.reload()', 1000);
          })
          .catch((error) => {
            this.ExeptionControl(error);
          })
      }

    },
    ExeptionControl(error) {
      this.exeptions = {
        name: '',
        date_time: null,
        place: '',
      }
      if (error.response.data.name) {
        const ex_name = error.response.data.name
        ex_name.forEach((expt) => {
          this.exeptions.name = expt;
        });
      }
      if (error.response.data.date_time) {
        const ex_date_time = error.response.data.date_time
        ex_date_time.forEach((expt) => {
          this.exeptions.date_time = expt;
        });
      }
      if (error.response.data.place) {
        const ex_place = error.response.data.place
        ex_place.forEach((expt) => {
          this.exeptions.place = expt;
        });
      }
    },
    EventDelete(event) {
      const path = `http://127.0.0.1:8000/api/v1.0/events/${event}/`;
      swal({
          title: "¿Está seguro de eliminar este evento?",
          icon: "warning",
          buttons: ['Cancelar', 'Eliminar'],
          dangerMode: true,
        })
        .then((willDelete) => {
          if (willDelete) {
            axios.delete(path);
            swal("Evento eliminado satisfactoriamente", {
              icon: "success",
              buttons: false,
            });
            setTimeout('document.location.reload()', 1000);
          }
        });
    },
    CleanForm() {
      this.event_obj = {
          id: null,
          name: null,
          date_time: null,
          place: null
        },
        this.exeptions = {
          name: '',
          date_time: null,
          place: '',
        }
    },
    // Contadores de eventos y visitantes
    CountersItems() {
      const path_events = "http://127.0.0.1:8000/api/v1.0/events/";
      const path_visitors = "http://127.0.0.1:8000/api/v1.0/visitors/";
      axios.get(path_events).then((response) => {
        this.counters.n_events = response.data.length;
      });
      axios.get(path_visitors).then((response) => {
        this.counters.n_visitors = response.data.length;
      })
    }
  },
  created() {
    //do something after creating vue instance
    this.EventList();
    this.CountersItems();
  },

}
</script>
<style lang="scss" scoped>
</style>
