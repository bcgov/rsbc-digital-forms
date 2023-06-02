import { Input } from "../common/Input/Input"
import "./commonForm.scss"

export const OfficerInfo = () => {

    return (
        <div className='officer-info border-design-form left'>
            <h3 >Officer</h3>
            <div>
                <div className="row" style={{ minHeight: '85px' }}>
                    <div className="col-sm-5" ><Input  className='field-height field-width' label="Last Name of Peace Officer Serving Prohibition Notice" name="officer-lastname"  type="text" required/></div>
                    <div className=" col-sm-3"><Input  className='field-height field-width' label="PRIME ID" name="officer-prime-id"  type="text" required/></div>
                    <div className=" col-sm-4"><Input  className='field-height field-width' label="Agency or RCMP Detachment" name="officer-agency"  type="text" required/></div>
                </div>
            </div>
        </div>
    )
}