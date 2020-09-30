from utils import positionSH

def front():
    return """
<body>
    <h1>Enter budget</h1>
    <form>
        <label>budget:</label>
        <input id="budgedQuery" type="text" value="2000000">
        <input id="submit" type="submit" value="GO" onclick="window.open(`/teambuilder?query=` + document.getElementById('budgedQuery').value)">
    </form>
</body> 
    """

def showResults(budget, data):
    html = """
        <body>
        <h1> Result for budget: {} </h1>
        <table>
        <tr>
            <th>
                Name
            </th>
            <th>
                Age
            </th>
            <th>
                Nationality
            </th>
            <th>
                Club
            </th>
            <th>
                Photo
            </th>
            <th>
                Overall
            </th>
            <th>
                Value
            </th>
            <th>
                Position
            </th>
        </tr>
        """.format(budget)
    for row in data:
        # for key in pos.keys():
        #     if row[7] in pos[key]:
        #         rowpos = key
        html += """
                <tr>
            <td>
                {}
            </td>
            <td>
                {}
            </td>
            <td>
                {}
            </td>
            <td>
                {}
            </td>
            <td>
                <img src="{}" alt="{}">
            </td>
            <td>
                {}
            </td>
            <td>
                {}
            </td>
                <td>
                {}
            </td>
            </tr>
            """.format(row[0], row[1], row[2], row[3], row[4], row[0], row[5], row[6], row[7])
    html += "</table></body>"
    return html