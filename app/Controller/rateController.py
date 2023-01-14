from app import app, render_template, request, jsonify, json
from app.Service import plansService, planCalculateService
from app.Repositoy import planRepository


@app.route("/")
def index():
    plans = plansService.PlansService(planRepository.PlansRepository)
    plan = plans.get_plans()
    code = plans.get_area_code()
    time = plans.get_call_time()
    return render_template("index.html", plan=plan, code=code, time=time)


@app.route("/calc_plan", methods=['POST'])
def calc_plan() -> float:
    data = request.get_json()
    origin = data["origin"]
    destiny = data["destiny"]
    timeCall = data["time"]
    plan = data["plan"]


    plans = plansService.PlansService(planRepository.PlansRepository)
    priceCall = plans.get_price_call(origin, destiny)


    if len(priceCall) == 0:
        priceWithoutPlan = 0
        pricewithPlan = 0
    else:
        price = priceCall[0][0]
        priceWithoutPlan = planCalculateService.calculate_without_plan(timeCall, price)
        if timeCall > plan:
            # minutos excedente
            surplusMin = planCalculateService.calculate_surplus(timeCall, plan)
            # multa por exceder
            indemnityPrice = planCalculateService.calculate_indemnity(price)
            pricewithPlan = planCalculateService.calculate_with_plan(surplusMin, indemnityPrice)
        else:
            pricewithPlan = 0


    result = {pricewithPlan, priceWithoutPlan}
    response = list(result)
    return sorted(response, key=int)
    # return priceCall