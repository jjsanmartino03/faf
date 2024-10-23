<script setup lang="ts">
import {PropType, ref} from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";
import {useTeamsStore, Team} from "../../store/teams";
import ProgressSpinner from "primevue/progressspinner";
import {usePlayersStore, Player} from "../../store/players.ts";

const visible = ref(false);
const props = defineProps({
  player: {
    type: Object as PropType<Partial<Player>>,
    default: null
  },
  editMode: {
    type: Boolean,
    default: false
  },
  categoryId: {
    type: Number,
    required: true
  },
  onCompleteAction: {
    required: false,
    type: Function as PropType<() => void>,
  }
})
const name = ref(props.player ? props.player.name : '');

const {createPlayer, statusCreatePlayer, getPlayers, updatePlayer} = usePlayersStore()


const onSubmit = async (e, editMode) => {
  e.preventDefault()

  let error = null
  if (editMode) {
    error = await updatePlayer(props.player.id, {
      name: name.value
    })
  } else {
    error = await createPlayer({
      name: name.value,
      team_category: props.categoryId
    })
  }

  if (error) return

  props.onCompleteAction && props.onCompleteAction()
  visible.value = false
}

</script>

<template>
  <Button v-if="editMode" @click="visible = true" icon="pi pi-pen-to-square"/>
  <Button v-else label="Nuevo Jugador" icon="pi pi-plus" class="mt-4" size="small" @click="visible = true"/>
  <Dialog :draggable="false" v-model:visible="visible" modal :header="editMode ? 'Editar jugador' : 'Crear jugador'"
          :style="{ width: '25rem' }">
    <form @submit.prevent="(e) => onSubmit(e,editMode)"
          class="flex flex-column w-full align-items-center justify-content-center">
      <div class="p-field mt-4">
        <FloatLabel>
          <label for="name">Nombre</label>
          <InputText required="true" id="name" v-model="name"/>
        </FloatLabel>
      </div>
      <div v-if="statusCreatePlayer != 'loading'" class="flex justify-end gap-2 mt-4">
        <Button type="button" label="Cancelar" severity="secondary" @click="visible = false"></Button>
        <Button type="submit" label="Guardar"></Button>
      </div>
      <div v-else class="flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 1.5rem; height: 1.5rem;"/>
      </div>
    </form>
  </Dialog>
</template>