# API QUẢN LÝ DỰ ÁN VÀ CÔNG VIỆC

## CÔNG NGHỆ SỬ DỤNG
* Sử dụng Django và Django Rest Framework
* Triển khai database Postgres với Docker
* Áp dụng xác thực JWT và phân quyền người dùng
## MÔ TẢ DỰ ÁN

### API ĐĂNG NHẬP VÀ ĐĂNG KÝ NGƯỜI DÙNG
* Đăng ký người dùng với vai trò khác nhau (Nhân viên, quản lý)
* API đăng nhập JWT
### API QUẢN LÝ DỰ ÁN 
* Tạo, sửa, xem xóa dự án
* Phân quyền truy cập vào dự án dựa trên vai trò người dùng
### API QUẢN LÝ CÔNG VIỆC
* Quản lý các nhiệm vụ trong mỗi dự án: thêm, sửa, xóa, và cập nhật trạng thái công việc (Đang tiến hành, Hoàn thành)
* Hỗ trợ gán nhiệm vụ cho người dùng cụ thể trong dự án

## HƯỚNG DẪN CHẠY
### TẠO MỖI TRƯỜNG ẢO VÀ CÀI THƯ VIỆN
* `python -m venv venv` 
* `source venv/scripts/activate` 
* `pip install -r requirements.txt` 
### TẠO FILE .ENV VÀ CÁC BIỂN CẦN THIẾT
* `touch .env`
* `echo USER_DATABASE = ... >> .env`
* `echo PASSWORD_DATABASE = ... >> .env`
* `echo PORT_DATABASE = ... >> .env`
* `echo NAME_DATABASE = ... >> .env`
* `echo HOST_DATABASE = ... >> .env`
* `echo SECRET_KEY = ...`
### KHỞI TẠO DATABASE
* `docker-compose up -d`
### CHẠY
* `python APIBackend/manage.py runserver`
