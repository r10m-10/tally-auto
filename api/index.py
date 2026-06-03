import requests
import uuid
import pandas as pd
import os
from dotenv import load_dotenv, set_key
from tkinter import filedialog
from flask import Flask, request, jsonify, render_template, session, redirect, url_for

def upd_form(blocks, selec_id, token):
    headers = {"Authorization" : f"Bearer {token}"}
    url = f"https://api.tally.so/forms/{selec_id}"
    payload = {
        "blocks": blocks
    }
    patch_headers = {**headers, "Content-Type": "application/json"}
    response = requests.patch(url, headers=patch_headers, json=payload)
    print(response.status_code, response.text)

def add_dropdown(name, blocks, dropdown_option):
    last = dropdown_option[-1]
    last["payload"]['isLast'] = False
    last_pos = blocks.index(last)
    count = len(dropdown_option)
    struct = {'uuid': '78945026-c733-4909-a063-ae435359a831', 'type': 'DROPDOWN_OPTION', 'groupUuid': last['groupUuid'], 'groupType': 'DROPDOWN', 'payload': {'isRequired': True, 'index': 7, 'isFirst': False, 'isLast': False, 'allowMultiple': True, 'text': 'prod_8'}}
    struct["uuid"] = str(uuid.uuid4())
    struct["payload"]["text"] = name
    struct["payload"]["index"] = count
    struct["payload"]["isLast"] = True
    dropdown_option.append(struct)
    blocks.insert(last_pos+1, struct)
    last = dropdown_option[-1]
    last_pos = blocks.index(last)

def add_price(name, ppu, blocks, calculated_fields):
    struct = {'uuid': 'e4efdaa7-7ecd-4135-a06e-9bd0ae394bed', 'name': 'price_9', 'type': 'NUMBER', 'value': 28}
    p_uid = str(uuid.uuid4())
    struct["uuid"] = p_uid
    struct["name"] = f"price_{name}"
    struct["value"] = ppu
    calculated_fields[0]['payload']['calculatedFields'].append(struct)
    struct_2 = {'uuid': 'db35dfd4-6db7-4198-9050-feb50661adf0', 'field': {'uuid': 'e4efdaa7-7ecd-4135-a06e-9bd0ae374bed', 'type': 'CALCULATED_FIELD', 'questionType': 'CALCULATED_FIELDS', 'blockGroupUuid': '139eaa76-c1c4-4bd1-8f31-1c0c0a3cca2b', 'title': 'price_1', 'calculatedFieldType': 'NUMBER'}}
    struct_2['uuid'] = str(uuid.uuid4())
    struct_2['field']['uuid'] = p_uid
    struct_2['field']['blockGroupUuid'] = calculated_fields[0]['groupUuid']
    struct_2['field']['title'] = f"price_{name}"
    blocks[0]['payload']['mentions'].append(struct_2)

def add_to_table(name, mrp, ppu, offer, expiry, blocks, info):
    last = info[-1]
    last_pos = blocks.index(last)

    struc_1 = {'uuid': '56fe11d3-f1f3-470d-85bb-f8ac7c70fc33', 'type': 'TEXT', 'groupUuid': 'b5735f4d-3ddb-4e4a-a1f3-f35aa559863d', 'groupType': 'TEXT', 'payload': {'columnListUuid': '3be57341-5458-49d6-a33f-2feda9acd3f8', 'columnUuid': 'a86fbf04-2435-4462-8513-9a50862e9a7f', 'columnRatio': 24, 'isHidden': True, 'safeHTMLSchema': [[]]}}
    struc_2 = {'uuid': '6cec98e4-8559-489d-88bf-b28e452cc22f', 'type': 'TEXT', 'groupUuid': '40a8b374-abc8-45c5-97a6-1fe6464445e2', 'groupType': 'TEXT', 'payload': {'columnListUuid': '3be57341-5458-49d6-a33f-2feda9acd3f8', 'columnUuid': 'a34148d8-a4b9-44cf-9dbd-1b979bcac123', 'columnRatio': 10, 'isHidden': True, 'safeHTMLSchema': [[]]}}
    struc_3 = {'uuid': 'db988010-475a-41ed-98f9-cb477becac49', 'type': 'TEXT', 'groupUuid': '253b67d7-6bbd-4f41-bac5-3952b03ae76e', 'groupType': 'TEXT', 'payload': {'columnListUuid': '3be57341-5458-49d6-a33f-2feda9acd3f8', 'columnUuid': '6bfa1125-347d-4fa5-a1a0-4b67876f465a', 'columnRatio': 18, 'isHidden': True, 'safeHTMLSchema': [[]]}}
    struc_4 = {'uuid': 'cf3423ad-8b3e-4d4a-8860-b80b5080c123', 'type': 'TEXT', 'groupUuid': 'bbff7832-f909-40f7-ad69-8196c0335b16', 'groupType': 'TEXT', 'payload': {'columnListUuid': '3be57341-5458-49d6-a33f-2feda9acd3f8', 'columnUuid': '87df5762-a1f5-4423-b16d-610dc0bf98c7', 'columnRatio': 10, 'isHidden': True, 'safeHTMLSchema': [[]]}}
    struc_5 = {'uuid': '963a7f03-addb-40f8-91ce-e03f95aaa1ba', 'type': 'TEXT', 'groupUuid': '645b6be5-b994-467b-a428-82a08e2cc871', 'groupType': 'TEXT', 'payload': {'columnListUuid': '3be57341-5458-49d6-a33f-2feda9acd3f8', 'columnUuid': '94715ef2-c23d-4ce2-98cf-e5deef6669f1', 'columnRatio': 14, 'isHidden': True, 'safeHTMLSchema': [[[['tag', 'div']]]]}}
    struc_6 = {'uuid': '69bab174-39cf-44cb-b68a-51e632c0f133', 'type': 'INPUT_NUMBER', 'groupUuid': '9c740b97-11a1-4f7b-a9e8-b6546a7e6f54', 'groupType': 'INPUT_NUMBER', 'payload': {'isRequired': False, 'columnListUuid': '3be57341-5458-49d6-a33f-2feda9acd3f8', 'columnUuid': '917a940d-728c-4a73-8bcd-d3362d132918', 'columnRatio': 14, 'name': 'qty_1', 'isHidden': True, 'placeholder': ''}}
    struc_7 = {'uuid': '166fad65-4d0b-478f-ad00-34bc02190354', 'type': 'TEXT', 'groupUuid': 'acb727ca-cfcc-49d1-a724-c7796b3dcf8a', 'groupType': 'TEXT', 'payload': {'columnListUuid': '3be57341-5458-49d6-a33f-2feda9acd3f8', 'columnUuid': '52cf9cdc-cc64-48d0-a354-374ffe63b6d0', 'columnRatio': 10, 'isHidden': True, 'safeHTMLSchema': [[[['tag', 'span'], ['mention']]], [' ']]}}

    uid = str(uuid.uuid4())
    struc_1['uuid'], struc_2['uuid'], struc_3['uuid'], struc_4['uuid'], struc_5['uuid'], struc_6['uuid'], struc_7['uuid'] = (str(uuid.uuid4()) for _ in range(7))
    struc_1['groupUuid'], struc_2['groupUuid'], struc_3['groupUuid'], struc_4['groupUuid'], struc_5['groupUuid'], struc_6['groupUuid'], struc_7['groupUuid'] = (str(uuid.uuid4()) for _ in range(7))
    struc_1['payload']['columnListUuid'] = struc_2['payload']['columnListUuid'] = struc_3['payload']['columnListUuid'] = struc_4['payload']['columnListUuid'] = struc_5['payload']['columnListUuid'] = struc_6['payload']['columnListUuid'] = struc_7['payload']['columnListUuid'] = uid
    struc_1['payload']['columnUuid'], struc_2['payload']['columnUuid'], struc_3['payload']['columnUuid'], struc_4['payload']['columnUuid'], struc_5['payload']['columnUuid'], struc_6['payload']['columnUuid'], struc_7['payload']['columnUuid'] = (str(uuid.uuid4()) for _ in range(7))
    mention = f"price_{name}"
    mention_id = ''

    for i in blocks[0]['payload']['mentions']:
        if i['field']['title'] == mention:
            mention_id = i['uuid']


    struc_1['payload']['safeHTMLSchema'][0].append(name)
    struc_2['payload']['safeHTMLSchema'][0].append(f"₹{mrp}")
    struc_3['payload']['safeHTMLSchema'][0].append(offer)
    struc_4['payload']['safeHTMLSchema'][0].append(f"₹{ppu}")
    struc_5['payload']['safeHTMLSchema'][0].insert(0, expiry)
    struc_6['payload']['name'] = f"qty_{name}"
    struc_7['payload']['safeHTMLSchema'][0].insert(0, f"@{mention}")
    struc_7['payload']['safeHTMLSchema'][0][1][1].append(mention_id)

    last = info[-1]
    last_pos = blocks.index(last)
    struc_li = [struc_1, struc_2, struc_3, struc_4, struc_5, struc_6, struc_7]

    for i in struc_li:
        blocks.insert(last_pos+1, i)
        info.append(i)
        last = info[-1]
        last_pos = blocks.index(last)

def add_conditiion(name, blocks, conditional_logic, dropdown_option):
    last = conditional_logic[-1]
    last_pos = blocks.index(last)

    struc = {'uuid': '4c7bea12-03d0-42e7-b3e3-f1fd67340559', 'type': 'CONDITIONAL_LOGIC', 'groupUuid': '4cf8eb2e-7aad-43a0-9ff8-5b233f191214', 'groupType': 'CONDITIONAL_LOGIC', 'payload': {'updateUuid': '916c8e0e-c05a-4609-8edf-8a04736b048f', 'logicalOperator': 'OR', 'conditionals': [{'uuid': '269ec597-3de4-4b45-9ba7-4287ee588fa2', 'type': 'SINGLE', 'payload': {'field': {'uuid': 'a5e4c785-aace-4faf-8e08-ce6119ca7d6f', 'type': 'INPUT_FIELD', 'questionType': 'DROPDOWN', 'blockGroupUuid': 'a5e4c785-aace-4faf-8e08-ce6119ca7d6f', 'title': 'Please select all applicable productsकृपाय सभी लागू वास्तु पर दबाये'}, 'comparison': 'CONTAINS', 'value': '22d98963-c213-48bd-9605-5aa06227e00d'}}], 'actions': [{'uuid': 'c16b2108-b976-4fa1-b813-83cd0f89170f', 'type': 'SHOW_BLOCKS', 'payload': {'showBlocks': ['56fe11d3-f1f3-470d-85bb-f8ac7c70fc33', '6cec98e4-8559-489d-88bf-b28e452cc22f', 'db988010-475a-41ed-98f9-cb477becac49', 'cf3423ad-8b3e-4d4a-8860-b80b5080c123', '963a7f03-addb-40f8-91ce-e03f95aaa1ba', '9c740b97-11a1-4f7b-a9e8-b6546a7e6f54', '166fad65-4d0b-478f-ad00-34bc02190354']}}, {'uuid': '2ff5780c-1c8a-462b-8f94-051cbd6a250e', 'type': 'REQUIRE_ANSWER', 'payload': {'requireAnswer': '9c740b97-11a1-4f7b-a9e8-b6546a7e6f54'}}, {'uuid': 'd85503af-0b4d-4a2f-9862-cac538c59aeb', 'type': 'CALCULATE', 'payload': {'calculate': {'field': {'uuid': 'e4efdaa7-7ecd-4135-a06e-9bd0ae374bed', 'type': 'CALCULATED_FIELD', 'questionType': 'CALCULATED_FIELDS', 'blockGroupUuid': '139eaa76-c1c4-4bd1-8f31-1c0c0a3cca2b', 'title': 'price_1', 'calculatedFieldType': 'NUMBER'}, 'operator': 'MULTIPLICATION', 'value': {'uuid': '9c740b97-11a1-4f7b-a9e8-b6546a7e6f54', 'type': 'INPUT_FIELD', 'questionType': 'INPUT_NUMBER', 'blockGroupUuid': '9c740b97-11a1-4f7b-a9e8-b6546a7e6f54', 'title': 'qty_1'}}}}, {'uuid': '8f007b39-50a7-4126-8219-770c04fd132b', 'type': 'CALCULATE', 'payload': {'calculate': {'field': {'uuid': '5195989c-97de-4132-90ca-e38f5d3ec613', 'type': 'CALCULATED_FIELD', 'questionType': 'CALCULATED_FIELDS', 'blockGroupUuid': 'f62f5a7a-0c19-4d23-8cbc-ed780494d6b1', 'title': 'tot_price', 'calculatedFieldType': 'NUMBER'}, 'operator': 'ADDITION', 'value': {'uuid': 'e4efdaa7-7ecd-4135-a06e-9bd0ae374bed', 'type': 'CALCULATED_FIELD', 'questionType': 'CALCULATED_FIELDS', 'blockGroupUuid': '139eaa76-c1c4-4bd1-8f31-1c0c0a3cca2b', 'title': 'price_1', 'calculatedFieldType': 'NUMBER'}}}}]}}
    price = f"price_{name}"
    qty = f"qty_{name}"
    prod_uid = prod_grp_uid = price_uid = price_grp_uid = tot_uid = tot_grp_uid = selec_uid = mrp_uid = offer_uid = ppu_uid = exp_uid = qty_uid = tot_txt_uid =  ''
    for i in blocks:
        if i["type"] == "DROPDOWN_OPTION":
            if i['payload']['text'] == name:
                prod_uid = i['uuid']
                prod_grp_uid = i['groupUuid']
        elif i["type"] == "CALCULATED_FIELDS":
            for j in i['payload']['calculatedFields']:
                if j['name'] == price:
                    price_uid = j['uuid']
                    price_grp_uid = i['groupUuid']
                elif j['name'] == "tot_price":
                    tot_uid = j['uuid']
                    tot_grp_uid = i['groupUuid']
        elif i["type"] == "TEXT":
            if i['payload']['safeHTMLSchema'][0][0] == name:
                selec_uid = i['uuid']
                mrp_uid = blocks[blocks.index(i)+1]['uuid']
                offer_uid = blocks[blocks.index(i)+2]['uuid']
                ppu_uid = blocks[blocks.index(i)+3]['uuid']
                exp_uid = blocks[blocks.index(i)+4]['uuid']
                qty_uid = blocks[blocks.index(i)+5]['groupUuid']
                tot_txt_uid = blocks[blocks.index(i)+6]['uuid']
        else:
            pass

    struc['uuid'] = str(uuid.uuid4())
    struc['groupUuid'] = str(uuid.uuid4())
    struc['payload']['updateUuid'] = str(uuid.uuid4())
    struc['payload']['conditionals'][0]['payload']['field']['uuid'] = prod_grp_uid
    struc['payload']['conditionals'][0]['payload']['field']['blockGroupUuid'] = prod_grp_uid
    struc['payload']['conditionals'][0]['payload']['value'] = prod_uid
    struc['payload']['actions'][0]['payload']['showBlocks'] = [selec_uid, mrp_uid, offer_uid, ppu_uid, exp_uid, qty_uid, tot_txt_uid]
    struc['payload']['actions'][1]['uuid'] = str(uuid.uuid4())
    struc['payload']['actions'][1]['payload']['requireAnswer'] = qty_uid
    struc['payload']['actions'][2]['uuid'] = str(uuid.uuid4())
    struc['payload']['actions'][2]['payload']['calculate']['field']['uuid'] = price_uid
    struc['payload']['actions'][2]['payload']['calculate']['field']['blockGroupUuid'] = price_grp_uid
    struc['payload']['actions'][2]['payload']['calculate']['field']['title'] = price
    struc['payload']['actions'][2]['payload']['calculate']['value']['uuid'] = qty_uid
    struc['payload']['actions'][2]['payload']['calculate']['value']['blockGroupUuid'] = qty_uid
    struc['payload']['actions'][2]['payload']['calculate']['value']['title'] = qty
    struc['payload']['actions'][3]['uuid'] = str(uuid.uuid4())
    struc['payload']['actions'][3]['payload']['calculate']['field']['uuid'] = tot_uid
    struc['payload']['actions'][3]['payload']['calculate']['field']['blockGroupUuid'] = tot_grp_uid
    struc['payload']['actions'][3]['payload']['calculate']['value']['uuid'] = price_uid
    struc['payload']['actions'][3]['payload']['calculate']['value']['blockGroupUuid'] = price_grp_uid
    struc['payload']['actions'][3]['payload']['calculate']['value']['title'] = price

    conditional_logic.append(struc)
    blocks.insert(last_pos+1, struc)
    last = dropdown_option[-1]
    last_pos = blocks.index(last)

def tally_api(token, selec_id=''):
    if selec_id == '':
        url = "https://api.tally.so/forms"
    else:
        url = f"https://api.tally.so/forms/{selec_id}"
    headers = {"Authorization" : f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    data= response.json()
    return data

def get_forms(data):
    f = data['items']
    forms = {}
    for i in f:
        forms[i["name"]] = i["id"]
    return forms

def form_struct(data):
    blocks = data["blocks"]
    calculated_fields = []
    dropdown_option = []
    conditional_logic = []
    info = []

    for i in blocks:
        if i["type"] == "DROPDOWN_OPTION":
            dropdown_option.append(i)
        elif i["type"] == "CALCULATED_FIELDS":
            if i["payload"]["calculatedFields"][0]["value"] != 0:
                calculated_fields.append(i)
        elif i["type"] == "CONDITIONAL_LOGIC":
            if i['payload']['conditionals'][0]['payload']['comparison'] == 'CONTAINS':
                conditional_logic.append(i)
        elif i["type"] == "TEXT" or i["type"] == "INPUT_NUMBER":
            info.append(i)
        else:
            pass
    info.pop()
    return blocks, calculated_fields, dropdown_option, conditional_logic, info

#path = filedialog.askopenfilename(title="Select products file",filetypes=[("CSV files", "*.csv")])
#ws = pd.read_csv(f"{path}", dtype=str, header=0)
#
#for i, row in ws.iterrows():
#    name, mrp, offer, ppu, exp = row
#    add_dropdown(name)
#    add_price(name, mrp)
#    add_to_table(name, mrp, ppu, offer, exp)
#    add_conditiion(name)
#
#    upd_form()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = "secretkey"

@app.route('/')
def index():
    if 'token' in session:
        return redirect(url_for('forms'))
    else:
        return render_template('index.html')
        
@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    exp = data['expression']
    session['token'] = exp
    return redirect(url_for('forms'))

@app.route('/forms')
def forms():
    token = session['token']
    data = tally_api(token)
    forms = get_forms(data)
    f_name = list(forms)
    session['forms'] = forms
    return render_template('forms.html', f_name=f_name)

@app.route('/update', methods=['POST'])
def update():
    pass

if __name__ == '__main__':
    app.run(debug=True)