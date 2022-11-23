import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className='w-[1100px] mx-auto '>
      <div className='flex justify-center mt-[60px] gap-[40px]'>
        <div className='border border-black w-[500px] mx-auto text-center rounded-[10px]  bg-white shadow-xl'>
          <div className='w-[500px] mx-auto' >
            <div className='mx-auto w-fit mt-10' >
              <Image src={'/school-books.jpg'} width={150} height={100}></Image>
            </div>
            <form action='http://127.0.0.1:8000/subscription' method='post'>
              <input type='hidden' value='124'></input>
              <input type='hidden' name='app_id' value='price_1M7A8KSERQhM1ogrR1CXc91m'></input>
              <div className='w-[150px] py-1 mx-auto bg-green-500 border mb-10 rounded-[4px] mt-10 shadow-xl' >
                <button className=' '>₹124.00 / month</button>
              </div>
            </form>
          </div>
        </div>
        <div className='border border-black w-[500px] mx-auto text-center rounded-[10px]  bg-white shadow-xl'>
          <div className='w-[500px] mx-auto' >
            <div className='mx-auto w-fit mt-10' >
              <Image src={'/school-books.jpg'} width={150} height={100}></Image>
            </div>
            <form action='http://127.0.0.1:8000/subscription' method='post'>
              <input type='hidden' name='app_id' value='price_1M7AEeSERQhM1ogr6ItKG76a'></input>
              <div className='w-[150px] py-1 mx-auto bg-green-500 border mb-10 rounded-[4px] mt-10 shadow-xl'>
                <button className=' '>₹1,240.00 / year</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  )
}
