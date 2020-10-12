<template>
<div class="has-background-white-ter">
  <div class="columns has-background-link">
    <div class="column">
      <div class="container py-3">
        <h1 class="title has-text-white is-size-1 ">Bienvenidos!</h1>
        <p class="subtitle has-text-white ">A continuación encontrarás una lista de enventos organizados por la empresa, sientete libre de registrate a cualquiera </p>
      </div>
    </div>

  </div>
  <section class="container mt-6">
    <div class="columns">
      <div class="column">
        <div class="box content" v-for="event in event_list">
          <article class="has-text-left">
            <h4>{{event.name}}</h4>
            <div class="media">
              <div class="media-content">
                <div class="content">
                  <p>
                    Fecha: {{event.date_time}}
                  </p>
                  <p>
                    Lugar: {{event.place}}
                  </p>
                </div>
              </div>
              <div class="media-right">
                <router-link :to="{ name: 'VisitorForm', params: {event_id: event.id}}" class="button is-primary is-outlined">
                  Registrar
                </router-link>
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>



</div>
</template>
<script>
import axios from 'axios';

export default {
  // name: "",
  data: () => ({
    event_list: []

  }),
  methods: {
    EventList() {
      const path = "http://127.0.0.1:8000/api/v1.0/events/"
      axios.get(path).then((response) => {
          this.event_list = response.data
        })
        .catch((error) => {
          alert(error);
        })
    },
  },
  created() {
    this.EventList();
  }
}
</script>
<style lang="scss" scoped>
</style>
