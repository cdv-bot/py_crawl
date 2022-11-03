import requests
from bs4 import BeautifulSoup


r = requests.get('https://api.github.com/user', auth=('cdv-bot', 'Ancoder92a'))

print(r.status_code)

url = "https://github.com"
page = 1

r = requests.get(url.format(page))
print('status_code', r.status_code)

# 2. Làm đẹp source
soup = BeautifulSoup(r.content, 'lxml')

# 3. Lấy block cha chứa tất cả các tags
# block_tag = soup.select_one('.tab-pane')
print(soup)

# 4. Các thẻ tag là con của block_tag, là các thẻ div có các class dưới đây
# all_tags = block_tag.select('.col-lg-4')


# 5. Viết hàm đọc các thông tin từ thẻ tag đó.
# Nếu option xử lý được bật, mình sẽ bỏ qua các khoảng trắng thừa, chỉ lấy giá trị số lượng
# def get_tag_info():
#     tag_name = all_tags[0].select_one(
#         'div.row > .col-lg-16.col-md-16.col-sm-8.col-xs-8>.product-item.no-padding>.pi-img-wrapper>img')[a"alt"]
#     print(tag_name)
#     return 12


# Thử in ra mà ko xử lý
# print(get_tag_info())