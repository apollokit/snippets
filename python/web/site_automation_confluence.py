import requests
import re

def remove_attachment_conf_page(space_name: str, page_name: str, file_name: str, session_id: str):
    """Remove an attachment from a page in a space in confluence

    Args:
        space_name: the space name
        page_name: page name
        file_name: file name for the attachment
        session_id: a session id cookie. You can get this by accessing the cookies in the dev 
            tools in your browser after logging into confluence. The name will be "JSESSIONID"
    """
    url = f'https://confluence.v.co/display/{space_name}/{page_name}'
    cookies = dict(JSESSIONID=session_id)
    r = requests.get(url, cookies=cookies)
    assert(r.status_code == 200)

    # match a string that looks like: <meta name="ajs-page-id" content="6129533">, and extract the content value
    matches = re.findall(r'<meta name="ajs-page-id" content="([0-9]*)">', str(r.content))
    # should only have one match for the page id
    assert(len(matches) == 1)
    page_id = int(matches[0])


    ## Query for attachment removal confirmation token
    # extract atl_token token from response

    file_name.replace(' ', '+')

    url = f'https://confluence.v.co/pages/confirmattachmentremoval.action?pageId={page_id}&fileName={file_name}'
    cookies = dict(JSESSIONID=session_id)
    r = requests.get(url, cookies=cookies)
    assert(r.status_code == 200)

    try:
        # match a string that looks like: <meta name="ajs-page-id" content="6129533">, and extract the content value
        matches = re.findall(r'<input type="hidden" name="atl_token" value="(\S*)">', str(r.content))
        # should only have one match for the page id
        assert(len(matches) == 1)
    except AssertionError:
        if re.search(r'Not Permitted - Confluence', str(r.content)):
            raise ValueError("Confluence responded 'not permitted'...this attachment doesn't exist")
        else:
            raise Exception('Unexpected response from confluence')
        
    atl_token = matches[0]

    ## Confirm the removal

    url = f'https://confluence.v.co/pages/removeattachment.action?pageId={page_id}&fileName={file_name}'

    r = requests.post(url, data={'atl_token': atl_token}, cookies=cookies)
    assert(r.status_code == 200)

if __name__ == '__main__':
    page_name = '2019-05-15'
    space_name = '~kkennedy'
    session_id = 'FD106155A8D2668DD41F095D3D288713'
    file_name = 'Screen Shot 2019-05-13 at 7.00.37 PM.png'
    remove_attachment_conf_page(space_name, page_name, file_name, session_id)
