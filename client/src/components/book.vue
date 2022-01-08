<template>
  <div class="container">
    <!-- 导航栏start -->
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button
            type="button"
            class="navbar-toggle collapsed"
            data-toggle="collapse"
            data-target="#bs-example-navbar-collapse-1"
            aria-expanded="false"
          >
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Brand</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li class="active">
              <a href="#">Link <span class="sr-only">(current)</span></a>
            </li>
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a
                href="#"
                class="dropdown-toggle"
                data-toggle="dropdown"
                role="button"
                aria-haspopup="true"
                aria-expanded="false"
                >Dropdown <span class="caret"></span
              ></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">Separated link</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li>
          </ul>
          <form class="navbar-form navbar-left">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search" />
            </div>
            <button type="submit" class="btn btn-default">Submit</button>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a
                href="#"
                class="dropdown-toggle"
                data-toggle="dropdown"
                role="button"
                aria-haspopup="true"
                aria-expanded="false"
                >Dropdown <span class="caret"></span
              ></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">Separated link</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- 导航栏end -->

    <!-- alert提示框start -->
    <alert :message="message" v-if="showMessage"></alert>
    <!-- alert提示框end -->

    <!-- 书籍内容start -->
    <h3>books</h3>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">题目</th>
          <th scope="col">作者</th>
          <th scope="col">Read?</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(book, index) in books" :key="index">
          <!-- 新版本必须搭配key使用 -->
          <!-- <tr v-for="(book, index) in books" :key="index"> -->
          <!-- {{book}} -->
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>
            <span v-if="book.read">读了</span>
            <span v-else>没读</span>
          </td>
          <td>
            <div class="btn-group" role="group">
              <button
                type="button"
                class="btn btn-success btn-sm"
                data-toggle="modal"
                data-target="#myModal2"
                @click="editBook(book)"
              >
                更新
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="onDeleteBook(book)"
              >
                Delete
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- Button trigger modal -->
    <button
      type="button"
      class="btn btn-primary btn-lg"
      data-toggle="modal"
      data-target="#myModal"
    >
      添加书籍
    </button>
    <!-- 书籍内容end -->

    <!-- 添加书籍的模态框start -->
    <div
      ref="addBookModal"
      class="modal fade"
      id="myModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="myModalLabel"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title" id="myModalLabel">添加书籍</h4>
          </div>
          <div class="modal-body">
            <form @submit="onSubmit" @reset="onReset">
              <div class="input-group">
                <span class="input-group-addon" id="basic-addon1">书名</span>
                <input
                  v-model="addBookForm.title"
                  type="text"
                  class="form-control"
                  placeholder="请输入书名"
                  aria-describedby="basic-addon1"
                />
              </div>
              <div class="input-group">
                <span class="input-group-addon" id="basic-addon2">作者</span>
                <input
                  v-model="addBookForm.author"
                  type="text"
                  class="form-control"
                  placeholder="请输入作者"
                  aria-describedby="basic-addon1"
                />
              </div>
              <label class="btn btn-primary active">
                <input
                  type="checkbox"
                  v-model="addBookForm.read"
                  value="true"
                />
                已经读了
              </label>
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-default"
                  data-dismiss="modal"
                >
                  关闭
                </button>
                <button type="reset" class="btn btn-default">重置</button>
                <button type="submit" class="btn btn-primary">保存</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- 添加书籍的模态框end -->

    <!-- 修改书籍信息的模态框start -->
    <div
      ref="addBookModal"
      class="modal fade"
      id="myModal2"
      tabindex="-1"
      role="dialog"
      aria-labelledby="myModalLabel"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="getBooks"
            >
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title" id="myModalLabel2">修改书籍信息</h4>
          </div>
          <div class="modal-body">
            <form @submit="onSubmitUpdate" @reset="onResetUpdate">
              <div class="input-group">
                <span class="input-group-addon" id="basic-addon3">书名</span>
                <input
                  v-model="editForm.title"
                  type="text"
                  class="form-control"
                  placeholder="请输入书名"
                  aria-describedby="basic-addon1"
                />
              </div>
              <div class="input-group">
                <span class="input-group-addon" id="basic-addon4">作者</span>
                <input
                  v-model="editForm.author"
                  type="text"
                  class="form-control"
                  placeholder="请输入作者"
                  aria-describedby="basic-addon1"
                />
              </div>
              <label class="btn btn-primary active">
                <input type="checkbox" v-model="editForm.read" value="true" />
                已经读了
              </label>
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-default"
                  data-dismiss="modal"
                  @click="getBooks"
                >
                  关闭
                </button>
                <button type="reset" class="btn btn-default">重置</button>
                <button type="submit" class="btn btn-primary">保存</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- 修改书籍信息的模态框end -->
  </div>
</template>

<script>
import axios from "axios";
import Alert from "./alert";
// const Alert = import('alert.vue')
export default {
  data() {
    return {
      books: [],
      //添加书籍的书籍
      addBookForm: {
        title: "",
        author: "",
        read: [],
      },
      editForm: {
        id: "",
        title: "",
        author: "",
        read: [],
      },
      message: "",
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    initForm() {
      //初始化
      this.addBookForm.title = "";
      this.addBookForm.author = "";
      this.addBookForm.read = [];
      this.editForm.id = "";
      this.editForm.title = "";
      this.editForm.author = "";
      this.editForm.read = [];
    },
    getBooks() {
      //获取数据
      const path = "http://localhost:5000/books";
      axios
        .get(path)
        .then((res) => {
          // console.log(res);
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onSubmit(evt) {
      //增加书籍--处理数据
      evt.preventDefault();
      // 用其他方法隐藏模态框会与preventDefault冲突
      $("#myModal").modal("hide");
      // this.$refs.addBookModal.hide();
      // $('#myModal').hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    addBook(payload) {
      //增加书籍--提交
      const path = "http://localhost:5000/books";
      axios
        .post(path, payload)
        .then((res) => {
          // console.log(res);
          this.getBooks();
          this.message = "成功添加书籍" + "《" + payload.title + "》";
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.showMessage = false;
          this.getBooks();
        });
    },
    onReset(evt) {
      //重置
      evt.preventDefault();
      $("#myModal").modal("hide");
      this.initForm();
    },

    //修改书籍信息
    editBook(book) {
      //初始化要修改或删除的书籍
      this.editForm = book;
    },
    onSubmitUpdate(evt) {
      //修改书籍--处理数据
      evt.preventDefault();
      $("#myModal2").modal("hide");
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updateBook(payload, this.editForm.id);
    },

    updateBook(payload, bookID) {
      //修改书籍--提交
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = "书籍信息已经更新";
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onResetUpdate(evt) {
      //重置
      evt.preventDefault();
      $("#myModal2").modal("hide");
      this.initForm();
      this.getBooks(); // 由于上面initForm清空了表单中的数据,同时双向绑定的效果也将当前的book对象数据给清空了,因此需要重新再get一次
    },

    onDeleteBook(book) {
      //删除
      let bookID = book.id;
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .delete(path)
        .then(() => {
          this.getBooks();
          this.message = "书籍" + "《" + book.title + "》" + "已经删除";
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
