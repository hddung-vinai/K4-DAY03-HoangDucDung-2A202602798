# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Hoàng Đức Dũng 
> **Mã Sinh Viên / Mã Học viên:** 2A202602798 
> **Chủ đề Lựa chọn:** *Trợ lý Dịch vụ Khách hàng VinBus:* Tra cứu lộ trình tuyến xe bus điện và đăng ký vé tháng.  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5/ 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 5/ 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 4/ 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 4/ 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **18/ 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "VinBus là gì và hiện có những loại dịch vụ nào?",
    "action_type": "FINAL_ANSWER",
    "thought": "OpenAI phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "VinBus là một dịch vụ vận tải công cộng sử dụng các phương tiện xe buýt hiện đại, thân thiện với môi trường, thuộc hệ sinh thái của Tập đoàn Vingroup. Dịch vụ này được cung cấp nhằm phục vụ nhu cầu di chuyển của người dân tại các đô thị và khu vực lân cận, với mục tiêu giảm ùn tắc giao thông và ô nhiễm môi trường.\n\nHiện tại, VinBus cung cấp một số loại dịch vụ chính như sau:\n\n1. **Xe buýt chở khách**: Cung cấp các tuyến xe buýt đi qua các khu vực đông dân cư, trung tâm thương mại, trường học, bệnh viện và các điểm du lịch.\n\n2. **Dịch vụ vé tháng**: Cho phép hành khách đăng ký vé tháng để tiết kiệm chi phí đi lại cho nhu cầu di chuyển thường xuyên.\n\n3. **VinBus đi điện**: Các xe buýt sử dụng công nghệ điện năng, giúp giảm thiểu ô nhiễm và tiếng ồn, tạo ra môi trường di chuyển thoải mái hơn cho hành khách.\n\n4. **Các dịch vụ đặc biệt**: Có thể có những dịch vụ như xe buýt đưa đón học sinh, hoặc xe buýt tuyến ngắn phục vụ các sự kiện đặc biệt, tùy thuộc vào nhu cầu của cộng động và khu vực hoạt động.\n\nVinBus không ngừng phát triển và mở rộng để phục vụ tốt hơn cho nhu cầu di chuyển của người dân.",
    "latency_ms": 4939.84
  },
  {
    "step": 1,
    "query": "Hãy tra cứu tuyến VinBus từ Mỹ Đình đến Hồ Tây.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "search_route",
    "arguments": {
      "origin": "Mỹ Đình",
      "destination": "Hồ Tây"
    },
    "observation": {
      "status": "SUCCESS",
      "type": "direct",
      "origin": "Mỹ Đình",
      "destination": "Hồ Tây",
      "routes": [
        {
          "route_name": "E01",
          "boarding_stop": "Bến xe Mỹ Đình",
          "alighting_stop": "Hồ Tây",
          "operating_time": "05:00 - 22:00",
          "frequency": "15 - 20 phút/chuyến"
        }
      ]
    },
    "latency_ms": 999.97
  },
  {
    "step": 2,
    "query": "Hãy tra cứu tuyến VinBus từ Mỹ Đình đến Hồ Tây.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Từ Mỹ Đình đến Hồ Tây, bạn có thể đi tuyến E01 (lên tại Bến xe Mỹ Đình, xuống tại Hồ Tây, giờ hoạt động 05:00 - 22:00, tần suất 15 - 20 phút/chuyến).",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Tôi muốn đăng ký vé tháng VinBus.",
    "action_type": "FINAL_ANSWER",
    "thought": "OpenAI phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Để giúp bạn đăng ký vé tháng VinBus, tôi cần một số thông tin sau:\n\n1. **Họ và tên của bạn**.\n2. **Đối tượng khách hàng**: Bạn là sinh viên hay khách hàng thông thường?\n3. **Số điện thoại liên hệ**.\n4. **Loại vé tháng**: Bạn muốn đăng ký vé tháng thường hay vé tháng sinh viên (nếu bạn là sinh viên)?\n\nVui lòng cung cấp các thông tin này nhé!",
    "latency_ms": 2102.58
  },
  {
    "step": 1,
    "query": "Tôi đang ở Mỹ Đình và muốn đến Hồ Tây. Hãy tìm tuyến VinBus phù hợp nhất cho tôi, cho biết tôi cần lên và xuống ở trạm nào, sau đó tư vấn loại vé tháng phù hợp.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "search_route",
    "arguments": {
      "origin": "Mỹ Đình",
      "destination": "Hồ Tây"
    },
    "observation": {
      "status": "SUCCESS",
      "type": "direct",
      "origin": "Mỹ Đình",
      "destination": "Hồ Tây",
      "routes": [
        {
          "route_name": "E01",
          "boarding_stop": "Bến xe Mỹ Đình",
          "alighting_stop": "Hồ Tây",
          "operating_time": "05:00 - 22:00",
          "frequency": "15 - 20 phút/chuyến"
        }
      ]
    },
    "latency_ms": 871.99
  },
  {
    "step": 2,
    "query": "Tôi đang ở Mỹ Đình và muốn đến Hồ Tây. Hãy tìm tuyến VinBus phù hợp nhất cho tôi, cho biết tôi cần lên và xuống ở trạm nào, sau đó tư vấn loại vé tháng phù hợp.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Từ Mỹ Đình đến Hồ Tây, bạn có thể đi tuyến E01 (lên tại Bến xe Mỹ Đình, xuống tại Hồ Tây, giờ hoạt động 05:00 - 22:00, tần suất 15 - 20 phút/chuyến).",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Tôi muốn đi VinBus từ một địa điểm không tồn tại đến Hồ Tây.",
    "action_type": "FINAL_ANSWER",
    "thought": "OpenAI phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Để tìm lộ trình từ một địa điểm không tồn tại đến Hồ Tây là không khả thi. Bạn hãy cung cấp tên địa điểm cụ thể mà bạn muốn xuất phát, tôi sẽ giúp bạn tìm lộ trình đến Hồ Tây.",
    "latency_ms": 1487.98
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 2 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
