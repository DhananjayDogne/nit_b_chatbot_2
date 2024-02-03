import './Nav.css';
import { RiArrowDropDownLine } from 'react-icons/ri';
import { Link } from 'react-router-dom';

const Chat = () => {
    return (
        <div className="nav">
            <Link to="/" className=' px-[4rem] font-bold text-3xl my-auto'>CareerMantri</Link>

            <ul className='pl-8 flex justify-between w-[35%] my-auto'>
                <li className='flex cursor-pointer'>Services <RiArrowDropDownLine className='m-auto text-3xl ' /></li>
                <Link to='/opportunityList' className='flex cursor-pointer'>Opportunity</Link>
                <li className='flex cursor-pointer'>About</li>
                <li className='flex cursor-pointer'>Contact</li>
            </ul>

            <div className="ml-auto my-auto pr-[6rem]">
                <a href='#' className='px-4 '>Login</a>
                <button className='px-4 w-auto py-2 w-[100px] text-black rounded-full bg-[#fff2de]'>Book Now</button>
            </div>

        </div>
    )
}

export default Chat;