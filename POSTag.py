from flask import request, jsonify, Blueprint
from datetime import datetime
import HMMTagger

postag = Blueprint("postag", __name__)


@postag.route("/autocomplete", methods=["GET"])
def autocomplete():
	start_time = datetime.now()
	langcode = request.args.get("lc")
	dataToTag = request.args.get("q")
	taggedData = HMMTagger.tagSentence(dataToTag, langcode)
	end_time = datetime.now()
	timeduration = end_time - start_time
	timeduration = timeduration.seconds + timeduration.microseconds / 1000000

	results = {
		"generated-from": langcode,
		"time": timeduration,
		"tagged-data": taggedData,
	}
	return jsonify(results=results)