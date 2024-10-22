<script setup lang="ts">
import { ref,watch } from "vue";
import Dialog from "primevue/dialog";
import FileUpload from "primevue/fileupload";
import { defineProps } from "vue";
import { defineEmits } from "vue";
import Button from "primevue/button";

const visible = ref(false);
const fileUploaded = ref(false);

const emit = defineEmits(['update:visible'])

const props = defineProps({
    visible: {
        type: Boolean,
        default: false
    }
})

const files = ref(null)

const onSubmit = async (e) => {
    e.preventDefault()

    let error = null

    if (error) return

    visible.value = false
}

const onAdvancedUpload = (e) => {
    console.log(e)
}

const handleFileUpload = (event) => {
  const file = event.files[0];
  fileUploaded.value = file ? true : false;
  files.value = event.files;
};

const onHide = () => {
    visible.value = false;
    fileUploaded.value = false;
}

const clearCallback = () => {
    fileUploaded.value = false;
}

watch(() => props.visible, (newVal) => {
  visible.value = newVal;
});

watch(() => visible.value, (newVal) => {
    emit('update:visible', newVal);
});
</script>

<template>
    <Dialog v-model:visible="visible" header="Subir imagen de validación de equipo" @hide="onHide">
        <template #header>
            <h3 class="mr-2">
                Subir imagen de validación de equipo
            </h3>
        </template>
        <template #default>
            <FileUpload name="demo[]" 
                :file-limit="1" 
                url="/api/upload" 
                accept="image/*" 
                :maxFileSize="1000000" 
                upload-label="Subir"
                cancel-label="Eliminar"
                cancel-icon="pi pi-times"
                choose-label="Elegir"
                @select="handleFileUpload"
                @remove="clearCallback"
                @clear="clearCallback"
            </FileUpload>
            <span v-if="!fileUploaded" class="p-info mt-2">
                <small>Seleccione una imagen para subir</small>
            </span>
        </template>
        <template #footer>
            <Button label="Cancelar" icon="pi pi-times" @click="visible = false"/>
        </template>
    </Dialog>
</template>