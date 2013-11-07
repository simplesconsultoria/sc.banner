*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close All Browsers

*** Variables ***

${TITLE} =  Electronic Frontier Foundation
${ID} =  electronic-frontier-foundation
${DESCRIPTION} =  Defending your rights in the digital world

${title_selector} =  input#form-widgets-IBasic-title
${description_selector} =  textarea#form-widgets-IBasic-description
${image_selector} =  input#form-widgets-image-input
${remote_url_selector} =  input#form-widgets-remote_url

*** Test cases ***

Test CRUD
    Enable Autologin as  Site Administrator
    Go to Homepage

    Create  ${TITLE}  ${DESCRIPTION}  http://eff.org/
    Update  https://www.eff.org/
    Delete

Test Redirection
    Enable Autologin as  Site Administrator
    Go to Homepage

    Create  ${TITLE}  ${DESCRIPTION}  https://www.eff.org/
    ${location} =  Set Variable  ${PLONE_URL}/${ID}/banner_redirect_view
    Location Should Be  ${location}

    # an anonymous user should be redirected
    Disable Autologin
    Open Browser  ${location}
    Location Should Be  https://www.eff.org/

*** Keywords ***

Create
    [arguments]  ${title}  ${description}  ${remote_url}

    Open Add New Menu
    Click Link  css=a#banner
    Page Should Contain  Add Banner
    Page Should Contain  Add Banner
    Input Text  css=${title_selector}  ${title}
    Input Text  css=${description_selector}  ${description}
    Choose File  css=${image_selector}  /tmp/banner.png
    Input Text  css=${remote_url_selector}  ${remote_url}
    Click Button  Save
    Check Status Message  Item created
    Check Status Message  You see this page because you have permission to edit this link.
    Page Should Contain  ${title}
    Page Should Contain  ${description}
    Page Should Contain Element  css=#content-core > p:nth-child(1) > img:nth-child(1)
    Page Should Contain  ${remote_url}

Update
    [arguments]  ${remote_url}

    Click Link  link=Edit
    Page Should Contain  Edit Banner
    Input Text  css=${remote_url_selector}  ${remote_url}
    Click Button  Save
    Check Status Message  Changes saved
    Page Should Contain  ${remote_url}

Delete
    Open Action Menu
    Click Link  css=a#plone-contentmenu-actions-delete
    Click Button  Delete
    Page Should Contain  Plone site
