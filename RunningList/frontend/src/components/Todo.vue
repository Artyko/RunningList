<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Task</button>
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
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td><b-form-checkbox v-if="book.read.includes('Mo')" value="true" v-model="book.Mo" @change=dayUpdate(book)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="book.read.includes('Tu')" value="true" v-model="book.Tu" @change=dayUpdate(book)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="book.read.includes('We')" value="true" v-model="book.We" @change=dayUpdate(book)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="book.read.includes('Th')" value="true" v-model="book.Th" @change=dayUpdate(book)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="book.read.includes('Fr')" value="true" v-model="book.Fr" @change=dayUpdate(book)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="book.read.includes('Sa')" value="true" v-model="book.Sa" @change=dayUpdate(book)></b-form-checkbox>
              </td>
              <td><b-form-checkbox v-if="book.read.includes('Su')" value="true" v-model="book.Su" @change=dayUpdate(book)></b-form-checkbox>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.book-update-modal
                          @click="editBook(book)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteBook(book)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBookModal"
            id="book-modal"
            title="Add a new book"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
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
    <b-modal ref="editBookModal"
            id="book-update-modal"
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
      books: [],
      addBookForm: {
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
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = this.addBookForm.read.toString();
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
    editBook(book) {
      this.editForm = book;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      let read = this.editBookModal.read.toString()
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updateBook(payload, this.editForm.id);
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Task updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks(); // why?
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book.id);
    },
    dayUpdate(book){
      const path = `http://localhost:5000/books/day/${book.id}`;
      const payload = {
        Mo: book.Mo,
        Tu: book.Tu,
        We: book.We,
        Th: book.Th,
        Fr: book.Fr,
        Sa: book.Sa,
        Su: book.Su,
      };
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
  },
  created() {
    this.getBooks()
  }
}
</script>
