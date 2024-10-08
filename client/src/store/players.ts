import { defineStore } from "pinia";
import { ref } from "vue";
import api from "../services/api.ts";
import { useToast } from "primevue/usetoast";

export type Player = {
    id: number
    name: string
    team_category: number
    status: boolean
    status_text: string
};

export const usePlayersStore = defineStore("players", () => {
  const toast = useToast();
  const players = ref<Player[] | null>(null);
  const player = ref<Player | null>(null);
  const statusGetPlayers = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
  const statusCreatePlayer = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
  const statusGetPlayer = ref<'loading' | 'success' | 'error' | 'idle'>('idle');

  async function getPlayers() {
    try {
      statusGetPlayers.value = 'loading';
      players.value = await api.get<Player[]>("api/players/");
      statusGetPlayers.value = 'success';
    } catch (e) {
      statusGetPlayers.value = 'error';
    }
  }

  async function createPlayer(player: Player) {
    statusCreatePlayer.value = 'loading';
    try {
      await api.post("api/players/", player);
      statusCreatePlayer.value = 'success';
        toast.add({ severity: 'success', summary: 'Juegador creado', detail: 'El jugador ha sido creado correctamente', life: 3000 });
    } catch (e) {
      statusCreatePlayer.value = 'error';
        toast.add({ severity: 'error', summary: 'Error', detail: 'Ha ocurrido un error al crear el jugador', life: 3000 });
    }
  }

  async function getPlayer(playerId: number) {
    statusGetPlayer.value = 'loading';
    try {
      const playerResult = await api.get<Player>(`api/players/${playerId}/`);
      player.value = playerResult;
      statusGetPlayer.value = 'success';
    } catch (e) {
      statusGetPlayer.value = 'error';
    }
  }

  return {
    players,
    player,
    statusGetPlayers,
    statusCreatePlayer,
    statusGetPlayer,
    getPlayers,
    createPlayer,
    getPlayer
  };
});
