
import requests
login_info = {
    'id' : "armada74",# clien id를 적습니다.
    'pw' : "westwood74"# password를 적습니다.
}
header = {"User-agent":'Mozilla/5.0'}
write_info = {
    'bo_table':'park',
    'wr_subject':"python으로 모두의 공원 글쓰기 test입니다.",
    'wr_content':"테스트 후 정리하여 팁과 강좌에 글올리겠습니다.\n 글은 곧 삭제됩니다.\n yangbeom",
    'wr_ccl_nc':"nc",
    'wr_ccl_nd':"nd"
}
with requests.Session() as s:
    r = s.post("https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fwww.naver.com", data = login_info, headers=header)
    print(r.text)
    # r = s.post("http://www.clien.net/cs2/bbs/write_update.php",data=write_info)