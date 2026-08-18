# Free2Do

**Nền tảng khám phá hoạt động dựa trên thời gian rảnh**

Free2Do giúp người dùng biến những khoảng thời gian rảnh ngắn, không cố định thành các trải nghiệm có giá trị — bằng cách gợi ý hoạt động phù hợp dựa trên **thời gian rảnh, vị trí, ngân sách và sở thích**, thay vì bắt người dùng phải tự biết mình muốn làm gì.

---

## 1. Vấn đề thực tế

Mọi người thường có những khoảng thời gian rảnh ngắn và không cố định nhưng lại không biết nên làm gì, đặc biệt khi muốn tìm một hoạt động phù hợp với thời gian, vị trí, ngân sách và sở thích hiện tại. Thông tin về các hoạt động đang phân tán trên Facebook, TikTok, Instagram, website và nhiều cộng đồng khác khiến việc tìm kiếm trở nên mất thời gian.

## 2. Mô hình vận hành

Người dùng nhập **thời gian rảnh, vị trí, ngân sách và sở thích**; hệ thống xếp hạng và đề xuất những hoạt động phù hợp nhất thay vì yêu cầu người dùng phải biết trước mình muốn làm gì.

- **Tìm kiếm đa tiêu chí**: loại hình, thời gian, giá, khoảng cách, hình thức online/offline, đối tượng tham gia.
- **Định vị & bản đồ**: xác định vị trí hiện tại (hoặc vị trí người dùng chọn), hiển thị hoạt động xung quanh, tính khoảng cách và ưu tiên hoạt động người dùng có đủ thời gian di chuyển tới.
- **Chấm điểm mức độ phù hợp**: kết hợp thời gian, khoảng cách, ngân sách, sở thích và lịch hoạt động — ví dụ một hoạt động có thể hiển thị "92% phù hợp".
- **Đánh giá sau trải nghiệm**: người dùng đánh giá chất lượng, trải nghiệm, mức độ phù hợp, viết nhận xét/chia sẻ hình ảnh — dữ liệu này dùng để cải thiện dần hệ thống đề xuất.

## 3. Chức năng cốt lõi

| Chức năng | Mô tả ngắn |
|---|---|
| Time Matching | Gợi ý hoạt động vừa khít với khoảng thời gian rảnh của người dùng |
| Location & Map | Định vị người dùng, hiển thị hoạt động quanh khu vực, tính khoảng cách |
| Budget Filtering | Lọc hoạt động theo ngân sách người dùng nhập |
| Interest Matching | Khớp hoạt động với sở thích/loại hình người dùng chọn |
| Recommendation | Chấm điểm % phù hợp và xếp hạng kết quả |
| Rating & Review | Đánh giá, nhận xét hoạt động sau khi tham gia |

## 4. Đối tượng người dùng

Mọi người có nhu cầu tận dụng thời gian rảnh — sinh viên, người đi làm, freelancer, nhóm bạn, cặp đôi... Điểm chung không phải tuổi tác hay nghề nghiệp, mà là nhu cầu: *"Tôi đang có một khoảng thời gian rảnh và muốn tìm một điều gì đó đáng để làm."*

## 5. Nguồn cung hoạt động

- **Giai đoạn đầu (MVP)**: Operator chủ động tìm kiếm, thu thập, xác minh hoạt động (workshop, lớp học, sự kiện, thể thao, giải trí, cộng đồng...) và chịu trách nhiệm cập nhật thời gian, địa điểm, giá, trạng thái.
- **Giai đoạn sau**: mở rộng nguồn từ doanh nghiệp, CLB, studio, trung tâm, nhà hàng, đơn vị tổ chức sự kiện — nhưng MVP vẫn quản lý dữ liệu tập trung qua Operator để đảm bảo tính khả thi.

## 6. Rủi ro

| Rủi ro | Hướng xử lý |
|---|---|
| **Dữ liệu** lỗi thời (thay đổi giờ/giá/địa điểm, bị hủy) | Hoạt động có trạng thái + thời hạn hiển thị, Operator kiểm tra định kỳ |
| **Độ tin cậy** (hoạt động giả, thông tin sai) | Xác minh trước khi đăng, cho phép người dùng báo cáo/đánh giá, Operator ẩn hoạt động bất thường |
| **Người dùng** không thực sự tham gia hoặc gợi ý chưa đúng | Theo dõi tỷ lệ click, lưu hoạt động, đánh giá sau trải nghiệm để tinh chỉnh thuật toán |
| **Phạm vi dự án** phình to (booking, thanh toán, chat, AI, mobile...) | MVP chỉ tập trung: tìm kiếm + bản đồ + matching + recommendation + đánh giá + quản trị hoạt động |

## 7. Tính khả thi

Triển khai dưới dạng **responsive web**, thử nghiệm tại một khu vực cụ thể (làm ở các quận nhỏ trước VD: **Hai Bà Trưng**), dữ liệu do Operator quản lý, recommendation dùng thuật toán scoring đơn giản. Bản đồ, tìm kiếm, đánh giá, quản lý dữ liệu và xác thực đều thực hiện được bằng công nghệ web phổ biến, không cần AI hay hệ thống phức tạp.

## 8. Giá trị của dự án

Free2Do không chỉ giúp "tìm chỗ đi chơi", mà giải quyết bài toán lớn hơn: biến thời gian rảnh thành trải nghiệm có giá trị — học kỹ năng mới, thử hoạt động mới, vận động, giải trí hoặc kết nối cộng đồng. Đồng thời tạo thêm kênh để các đơn vị tổ chức hoạt động tiếp cận đúng người đang có thời gian và nhu cầu.

---

## 9. Công nghệ sử dụng

### Frontend

| Công cụ | Loại | Mục đích sử dụng trong Free2Do |
|---|---|---|
| HTML | Ngôn ngữ nền tảng | Xây dựng cấu trúc các trang: trang chủ (nhập thời gian rảnh/sở thích), trang kết quả tìm kiếm, trang chi tiết hoạt động, trang đánh giá, trang quản trị Operator |
| CSS | Ngôn ngữ nền tảng | Định dạng giao diện, bố cục responsive |
| JavaScript | Ngôn ngữ nền tảng | Xử lý logic: lọc dữ liệu (`filter()`, `sort()`), hiển thị hoạt động động (`innerHTML`), xử lý sự kiện (click, submit form) |
| Bootstrap | Framework CSS (nhúng qua CDN) | Tạo giao diện đẹp, responsive nhanh cho: card hiển thị hoạt động (kèm % phù hợp), thanh filter (ngân sách, loại hình), form nhập liệu |
| Geolocation API | Web API có sẵn của trình duyệt | Lấy tọa độ (kinh độ, vĩ độ) vị trí hiện tại của người dùng làm điểm gốc tính khoảng cách |
| Fetch API | Web API có sẵn của trình duyệt | Gọi dữ liệu từ backend: gửi yêu cầu tìm kiếm, lấy danh sách hoạt động, gọi endpoint tính khoảng cách đường đi, gửi đánh giá sau khi tham gia |
| LocalStorage API | Web API có sẵn của trình duyệt | Lưu tạm tọa độ người dùng và dữ liệu tìm kiếm (thời gian, ngân sách, sở thích) khi chuyển giữa các trang `.html` |

### Backend

| Công cụ | Loại | Mục đích sử dụng trong Free2Do |
|---|---|---|
| Python | Ngôn ngữ lập trình | Xây dựng logic backend, xử lý dữ liệu, kết nối và thao tác với cơ sở dữ liệu |
| FastAPI | Framework backend (Python) | Xây dựng REST API: định nghĩa endpoint, validate dữ liệu (Pydantic), xử lý request/response bất đồng bộ, tự sinh tài liệu API (Swagger) |
| PostgreSQL | Hệ quản trị CSDL quan hệ | Lưu trữ dữ liệu chính của hệ thống: người dùng, hoạt động, đánh giá... đảm bảo tính toàn vẹn dữ liệu |
| PostGIS | Extension không gian địa lý (chạy trên PostgreSQL) | Lưu tọa độ, xử lý truy vấn không gian: tìm địa điểm gần nhất, kiểm tra vị trí trong bán kính — phục vụ chức năng bản đồ/vị trí |
| Supabase | Backend-as-a-Service (hosting DB) | Cung cấp PostgreSQL/PostGIS được quản lý sẵn, kèm Authentication, Storage, Realtime API — giảm thời gian dựng hạ tầng |

---

## 10. Cấu trúc thư mục

```
free2do/
├── frontend/
│   ├── index.html            # Trang chủ - nhập thời gian/ngân sách/sở thích
│   ├── search-results.html   # Trang kết quả tìm kiếm
│   ├── activity-detail.html  # Trang chi tiết hoạt động
│   ├── review.html           # Trang đánh giá
│   ├── admin.html            # Trang quản trị Operator
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── main.js           # Helper dùng chung: Fetch API, LocalStorage, Geolocation
│       ├── search.js
│       ├── results.js
│       ├── detail.js
│       ├── review.js
│       └── admin.js
└── backend/
    ├── app/
    │   ├── main.py
    │   ├── config.py
    │   ├── database.py
    │   ├── models.py
    │   ├── schemas.py
    │   ├── routers/
    │   │   ├── activities.py
    │   │   ├── search.py
    │   │   ├── reviews.py
    │   │   └── operator.py
    │   └── utils/
    │       └── distance.py
    ├── requirements.txt
    └── .env.example
```

## 11. Hướng dẫn chạy dự án

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # điền thông tin kết nối Supabase/PostgreSQL
uvicorn app.main:app --reload
```
API mặc định chạy tại `http://localhost:8000`, tài liệu Swagger tại `http://localhost:8000/docs`.

### Frontend
Mở trực tiếp `frontend/index.html` bằng trình duyệt, hoặc dùng Live Server để tránh vấn đề CORS/Geolocation:
```bash
cd frontend
npx live-server
```

---

## 12. Thành viên nhóm

| Vai trò | Họ và tên | Nhiệm vụ chính |
|---|---|---|
| Project Manager (PM) | *Nguyễn Thiện Nhân* | Lên kế hoạch, phân công công việc, theo dõi tiến độ, quản lý rủi ro dự án |
| UI/UX Designer | *Lê Thị Diệu Linh* | Thiết kế wireframe, luồng người dùng, giao diện các trang |
| System Architect | *Dương Khánh Duy* | Thiết kế kiến trúc hệ thống, sơ đồ CSDL, luồng dữ liệu frontend-backend |
| Frontend Developer | *Phạm Phương Anh* | Xây dựng giao diện HTML/CSS/JS, tích hợp Bootstrap, gọi API bằng Fetch |
| Backend Developer | *Đoàn Anh Tú* | Xây dựng REST API bằng FastAPI, thiết kế và triển khai CSDL PostgreSQL/PostGIS |
| QA/Tester | *Trần Hoàng Trung* | Viết test case, kiểm thử chức năng, báo cáo và theo dõi lỗi |
| Thư ký + Triển khai | *Nguyễn Thị Linh Anh* | Ghi biên bản họp, tổng hợp tài liệu, triển khai (deploy) hệ thống |

---

## 13. Phạm vi MVP

Tìm kiếm + Bản đồ + Matching + Recommendation + Đánh giá + Quản trị hoạt động.
