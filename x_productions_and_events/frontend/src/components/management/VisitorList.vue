<template>
<div id="visitor" class="has-background-white-ter">
  <Navbar />
  <div class="columns mt-2">
    <div class="column is-10 is-offset-1 pt-5">
      <h1 class="title is-pulled-left">Lista de Visitantes</h1>
      <router-link :to="{ name: 'Management'}" class="button is-primary is-rounded is-pulled-right">Regresar</router-link>
    </div>

  </div>
  <div class="columns has-text-left">
    <div class="column is-10 is-offset-1">
      <div class="card">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th v-for="item in table_header">{{item}}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="visitor in visitors">
              <td>{{visitor.name}}</td>
              <td>{{visitor.last_name}}</td>
              <td>{{visitor.document_id}}</td>
              <td>{{visitor.city}}</td>
              <td>{{visitor.company_name}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>



  </div>
</div>
</template>
<script>
import Navbar from '@/components/management/Navbar';

import axios from 'axios';

export default {

  name: "VisitorList",
  components: {
    Navbar
  },
  data: () => ({
    table_header: ['Nombre', 'Apellido', 'documento', 'Ciudad', 'Empresa'],
    visitors: {},
  }),
  methods: {
    get_visitors() {
      const path = `http://127.0.0.1:8000/api/v1.0/get_visitors/${this.$route.params.event_id}/`;
      axios.get(path).then((response) => {
        this.visitors = response.data;
      })
    },
  },
  created() {
    //do something after creating vue instance
    this.get_visitors();
  }
}
</script>
<style lang="scss" scoped>
</style>
