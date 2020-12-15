<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Task</th>
              <th scope="col">Mo</th>
              <th scope="col">Tu</th>
              <th scope="col">We</th>
              <th scope="col">Th</th>
              <th scope="col">Fr</th>
              <th scope="col">Sa</th>
              <th scope="col">Su</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(task, index) in tasks" :key="index">
              <td>{{ task.title }}</td>
              <td><b-form-checkbox v-if="task.read.includes('Mo')" value="true" v-model="task.Mo" @change=dayUpdate(task)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="task.read.includes('Tu')" value="true" v-model="task.Tu" @change=dayUpdate(task)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="task.read.includes('We')" value="true" v-model="task.We" @change=dayUpdate(task)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="task.read.includes('Th')" value="true" v-model="task.Th" @change=dayUpdate(task)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="task.read.includes('Fr')" value="true" v-model="task.Fr" @change=dayUpdate(task)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="task.read.includes('Sa')" value="true" v-model="task.Sa" @change=dayUpdate(task)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="task.read.includes('Su')" value="true" v-model="task.Su" @change=dayUpdate(task)></b-form-checkbox>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.task-update-modal
                          @click="edittask(task)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeletetask(task)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addtaskModal"
            id="task-modal"
            title="Add a new task"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addtaskForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addtaskForm.read" id="form-checks">
            <b-form-checkbox value="Mo">Mo</b-form-checkbox>
            <b-form-checkbox value="Tu">Tu</b-form-checkbox>
            <b-form-checkbox value="We">We</b-form-checkbox>
            <b-form-checkbox value="Th">Th</b-form-checkbox>
            <b-form-checkbox value="Fr">Fr</b-form-checkbox>
            <b-form-checkbox value="Sa">Sa</b-form-checkbox>
            <b-form-checkbox value="Su">Su</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="edittaskModal"
            id="task-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="Mo">Mo</b-form-checkbox>
            <b-form-checkbox value="Tu">Tu</b-form-checkbox>
            <b-form-checkbox value="We">We</b-form-checkbox>
            <b-form-checkbox value="Th">Th</b-form-checkbox>
            <b-form-checkbox value="Fr">Fr</b-form-checkbox>
            <b-form-checkbox value="Sa">Sa</b-form-checkbox>
            <b-form-checkbox value="Su">Su</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
export default {
  data() {
    return {
      tasks: [],
      addtaskForm: {
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    gettasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addtask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then(() => {
          this.gettasks();
          this.message = 'task added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.gettasks();
        });
    },
    initForm() {
      this.addtaskForm.title = '';
      this.addtaskForm.author = '';
      this.addtaskForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addtaskModal.hide();
      let read = this.addtaskForm.read.toString();
      const payload = {
        title: this.addtaskForm.title,
        author: this.addtaskForm.author,
        read, // property shorthand
      };
      this.addtask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addtaskModal.hide();
      this.initForm();
    },
    edittask(task) {
      this.editForm = task;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.edittaskModal.hide();
      let read = this.edittaskModal.read.toString()
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updatetask(payload, this.editForm.id);
    },
    updatetask(payload, taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.put(path, payload)
        .then(() => {
          this.gettasks();
          this.message = 'Task updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.gettasks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.edittaskModal.hide();
      this.initForm();
      this.gettasks(); // why?
    },
    removetask(taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.delete(path)
        .then(() => {
          this.gettasks();
          this.message = 'task removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.gettasks();
        });
    },
    onDeletetask(task) {
      this.removetask(task.id);
    },
    dayUpdate(task){
      const path = `http://localhost:5000/tasks/day/${task.id}`;
      const payload = {
        Mo: task.Mo,
        Tu: task.Tu,
        We: task.We,
        Th: task.Th,
        Fr: task.Fr,
        Sa: task.Sa,
        Su: task.Su,
      };
      axios.put(path, payload)
        .then(() => {
          this.gettasks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.gettasks();
        });
    },
  },
  created() {
    this.gettasks()
  }
}
</script>
