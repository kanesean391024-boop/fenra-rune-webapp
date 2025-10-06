from flask import Flask, render_template, request
import rune_agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    rune_output = ""
    flavor_text = ""
    user_input = ""
    log_entries = rune_agent.read_log()
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            runes, flavor = rune_agent.translate_to_runes(user_input)
            rune_output = runes
            flavor_text = flavor
            rune_agent.log_translation(user_input, runes)
            log_entries = rune_agent.read_log()  # Refresh log
    return render_template("index.html", rune_output=rune_output, flavor_text=flavor_text, user_input=user_input, log_entries=log_entries)
if __name__ == "__main__":
    app.run(debug=True)
