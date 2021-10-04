<template>
    <div class="page-dashboard">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Pesquisa de satisfação</h1>
                <div class="columns">
                <div class="column is-4 is-offset-4">
                <h1 class="text">Nivel de importância:</h1>
                <div class="control">
                  <label class="radio">
                    <input type="radio" name="answer">
                    Alta
                  </label>
                </div>
                <div class="control">
                  <label class="radio">
                    <input type="radio" name="answer">
                    Média
                  </label>
                </div>
                <div class="control">
                  <label class="radio">
                    <input type="radio" name="answer">
                    Baixa
                  </label>
                </div>
            </div>
            <div class="column is-one-quarter">

            </div>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Dashboard'
}
</script>