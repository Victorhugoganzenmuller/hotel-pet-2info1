<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import { buscarTutor } from '@/services/tutores';

const route = useRoute();
const tutor = ref(null);
const carregando = ref(true);
const erro = ref('');

async function carregarTutor() {
  carregando.value = true;
  erro.value = '';

  try {
    tutor.value = await buscarTutor(route.params.id);
    if (!tutor.value || !tutor.value.id) {
      erro.value = 'Tutor não encontrado.';
    }
  } catch (error) {
    erro.value = `Erro ao carregar tutor: ${error.message}`;
  } finally {
    carregando.value = false;
  }
}

onMounted(carregarTutor);
</script>

<template>
  <div>
    <header class="mb-4">
      <h1 class="h2">Detalhes do tutor</h1>
    </header>

    <p v-if="carregando" class="text-body-secondary" role="status">
      Carregando tutor...
    </p>

    <p v-else-if="erro" class="alert alert-danger" role="alert">
      {{ erro }}
    </p>

    <dl v-else class="row">
      <dt class="col-sm-2">ID</dt>
      <dd class="col-sm-10">{{ tutor.id }}</dd>

      <dt class="col-sm-2">Nome</dt>
      <dd class="col-sm-10">{{ tutor.nome }}</dd>

      <dt class="col-sm-2">Telefone</dt>
      <dd class="col-sm-10">{{ tutor.telefone }}</dd>
    </dl>

    <RouterLink class="btn btn-outline-secondary" :to="{ name: 'tutores' }">
      Voltar para tutores
    </RouterLink>
  </div>
</template>
