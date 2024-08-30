import {defineStore, Store, StoreDefinition} from "pinia";
import api from "../services/api.ts";

type LoginResponse = {
  token: string
}

type User = any

type AuthStore = {
  token: string | null
  isAuthenticated: boolean
  user: User | null
}

export const useAuthStore: StoreDefinition<"auth", AuthStore> = defineStore('auth', {
  state: () => ({
    token: null,
    isAuthenticated: localStorage.getItem('token') !== null,
    user: null
  }),
  actions: {
    async login(username, password) {

      try {
        const response = await api.post<LoginResponse>('api-auth/', {username, password})

        this.token = response.token
        localStorage.setItem('token', response.token)
        this.isAuthenticated = true
        return true
      } catch (e) {
        alert('Error al iniciar sesión, intente nuevamente')
        return false
      }
    },
    logout() {
      this.token = null
      this.isAuthenticated = false
      localStorage.removeItem('token')
    },
    async getCurrentUser() {
      try {
        const response = await api.get('api/user/')
        this.user = response.data
      } catch (e) {
        alert('Error al obtener el usuario')
        return false
      }
    }
  }
})